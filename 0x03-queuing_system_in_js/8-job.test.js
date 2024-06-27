import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach((done) => {
    queue.testMode.enter(); // Enter test mode before each test
    done();
  });

  afterEach((done) => {
    queue.testMode.clear(); // Clear all jobs in the queue after each test
    queue.testMode.exit(); // Exit test mode after each test
    done();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;
    expect(jobsInQueue).to.have.lengthOf(2);
    expect(jobsInQueue[0].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[1].type).to.equal('push_notification_code_3');
  });
});
