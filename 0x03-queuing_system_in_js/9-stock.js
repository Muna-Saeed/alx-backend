// Product data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Function to retrieve product by itemId
function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}


import express from 'express';
import redis from 'redis';
import { promisify } from 'util';


const app = express();
const port = 1245;

app.use(express.json());

// Redis client setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity
  })));
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(parseInt(itemId));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
    currentQuantity
  });
});

// Route to reserve product by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(parseInt(itemId));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity >= product.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId: product.itemId });
    return;
  }

  await reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: 'Reservation confirmed', itemId: product.itemId });
});

// Function to reserve stock in Redis
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Function to get current reserved stock from Redis
async function getCurrentReservedStockById(itemId) {
  const value = await getAsync(`item.${itemId}`);
  return value ? parseInt(value) : 0;
}

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
