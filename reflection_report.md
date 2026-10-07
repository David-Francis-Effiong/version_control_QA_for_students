# Reflection Report

**Challenges Faced**
While learning Git, Continuous Integration (CI), and Quality Assurance (QA) tools, one of the primary challenges was understanding the branching mechanism and how to properly resolve merge conflicts when collaborating. Additionally, setting up the CI pipeline initially caused some confusion because the YAML syntax must be strictly formatted, and debugging failed builds directly from the GitHub interface can feel less intuitive than working locally. 

**Streamlining the Development Process with CI**
The CI pipeline significantly streamlined the development process by automating the tedious task of manually testing code after every change. Whenever someone pushed a new commit or opened a pull request, the pipeline instantaneously checked if the code would build and pass all unit tests. This early detection mechanism drastically minimized the chance of deploying broken code to the main branch, allowing the team to iterate quickly without fear of causing regressions.

**Improving Collaboration and Quality**
Using Git alongside QA practices completely transformed our collaboration. Version control gave us the freedom to develop new features in isolation and securely merge them only after review. Incorporating a linter and unit tests as part of our QA meant that code formatting debates were solved by an automated standard, and any functional mistakes were caught during the CI phase rather than down the line. Ultimately, this integration enforced a discipline that yielded much cleaner, more reliable code.
