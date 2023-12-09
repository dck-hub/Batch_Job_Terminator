
<h1 align="center">Batch_Job_Terminator</h1>

<p> <ol>
<li>As a DevOps practitioner, i need to take care of the AWS environment Cost and Make sure all the environments are down in non-working hours. I use AWS EventBridge Rules in combination with AWS Lambda to capture the batch jobs that running in AWS ECS service. </li>
<li>.In this repository, I trigger a Lambda function when a AWS Batch Job is Started running (ecs tasks).I set up EventBridge Rule to capture that particular Batch job ID and jod Queue and will Terminate the jobs that were previously printed and are still in the STARTING state </li>

</ol>
</p>
