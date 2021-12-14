# Engineering Project - Backend API

Please read through this entire document to ensure requirements are not missed. While the completeness of your project submission is important, we will also use your stack choice and architecture decisions to understand how you solve problems.

Some requirements are left intentionally ambiguous, so feel free to make and document assumptions. If you'd like help or feedback with something you're stuck on feel free to reach out by email - pretend I'm another experienced engineer on your team but not on the same project.

## Ground Rules
To keep the hiring process as fair as possible, we would like this to be original code rather than something you've written previously, borrowed from a friend, or found on the internet. Of course, including and leveraging libraries and frameworks are fair game and encouraged. Keep in mind if you choose to use a framework, we may ask follow up questions about why you chose to use it and how it works under the hood.

We also ask that you check in your submission to a public GitHub repository. Please use discretion in how you name your project.

## Build a Simple Messenger API
We'd like you to build a simplified messenger API that would enable a web app to build a simple messaging application.

### High Level Requirements
Build an API that supports a web-application to enable two users to send short text messages to each other, like Facebook Messages app or Google Chat.

Ignore Authorization, Authentication and Registration. Assume this is a global API that can be leveraged by anyone, security implementation is not a concern.

1. A short text message can be sent from one user (the sender) to another (the recipient).
2. Recent messages can be requested for a recipient from a specific sender
  a) By default, only messages from the last 30 days should be returned. Additionally, there should be a limit of 100 messages in a response.
3. Recent messages can be requested from all senders
  a) By default, only messages from the last 30 days should be returned. Additionally,
there should be a limit of 100 messages in a response.
4. Document your API like you would be presenting to a frontend/web team for use.
5. Include tests and document how to test your API.
6. Document how to install dependencies needed to run your API.
7. Ensure we can start and invoke your API. Production software does not run in an IDE.
8. Curl commands are sufficient for hitting your API, no UI or frontend is necessary.

### Other Considerations
Here are some additional considerations to help you decide what and how much to build:
1. We're only expecting a couple hours to a half day of effort, please spend no more than eight hours on this project. Consider speed of development a trade off and document your decisions.
2. You cannot assume that everyone runs the same OS or even architecture as your local machine.
3. 3. If you get stuck and don't feel like you can finish this in a short amount of time (or at all), that's fine; just build what you can and supplement it with a detailed written description/design on where things ended up, where you would go next with more time, and be ready to talk about it.
4. Be prepared to discuss how you might implement authentication and authorization.

## Evaluation
Final code project in a ready to build/run state along with a README/instructions, notes, and any other related documentation should be checked into a public GitHub repository. Please email the link to the repository within the time communicated by the recruiter.

Creativity, clarity, design decisions, understanding the challenges of the problem, and being able to extrapolate further if/when we discuss it are more important than the volume of code written.
