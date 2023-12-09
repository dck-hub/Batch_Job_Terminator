import json
import boto3

# Initialize AWS Batch client
batch = boto3.client('batch')

# List to store the job IDs of jobs in the STARTING state
starting_jobs = []

def print_new_running_jobs(event, context):
    global starting_jobs

    try:
        # Extract job details from the event
        detail = event['detail']
        
        # Check if the job is in the STARTING state
        if detail['status'] == 'STARTING':
            job_id = detail['jobId']
            job_queue = detail['jobQueue']

            print(f'Newly running batch job in queue {job_queue}. Job ID: {job_id}')

            # Add the job ID to the list of starting jobs
            starting_jobs.append(job_id)

            # Terminate jobs that were previously printed and are still in the STARTING state
            for starting_job_id in starting_jobs:
                try:
                    response = batch.describe_jobs(jobs=[starting_job_id])
                    job_status = response['jobs'][0]['status']
                    if job_status == 'STARTING':
                        print(f'Terminating previously printed job in STARTING state. Job ID: {starting_job_id}')
                        batch.terminate_job(jobId=starting_job_id, reason='Terminating previously printed job')
                except batch.exceptions.ClientError as e:
                    print(f'Error terminating job: {str(e)}')

    except Exception as e:
        print(f'Error: {str(e)}')

    return {
        'statusCode': 200,
        'body': 'Lambda execution completed.'
    }
