# GitHub Lab 2: Inheritance with Classes

## Student Information

* Kioma Montoya
* Spring 2026
* CRN

## Instructions

In this lab, you will be focusing two elements of a contact information using concepts of inheritance, class variables, and exception handling. You only will be required to pass the unit test in order to complete the submission.

---

### Class: Contact

Below are the **attributes** for the class Contact. These attributes **ONLY** exist in this class and are inherited in the other two classes.

* `self.name_first`
* `self.name_last`

Below are the **class variables** for the class Contact. This class variable **ONLY** exists in this class and is accessible in the other two classes via inheritance.

* `contact_list`

Below are the **methods** for the class Contact. These methods **ONLY** exist in this class and are inherited in the other two classes.

* `get_name_first(self)`: Returns the attribute name_first
* `set_name_first(self, value)`: Sets the provided value for the attribute name_first
* `get_name_last(self)`: Returns the attribute name_last
* `set_name_last(self, value)`: Sets the provided value for the attribute name_last

---

### Class: ContactEmail

Below are the **attributes** for the class ContactEmail. These attributes **ONLY** exist in this class.

* `self.email`

Below are the methods for class ContactEmail:

* `validate(self, email)`: Validates the email parameter using the basic email pattern `address@domain.com` and returns true/false
* `set_info(self, value)`: Will validate the value parameter as an email, set the email address in the self.email attribute & store the object in the contact_list class variable; if validation is false, raise a `ValueError`
* `get_info(self)`: Returns the self.email attribute

---

### Class: ContactPhone

Below are the **attributes** for the class ContactPhone. These attributes **ONLY** exist in this class.

* self.phone

Below are the methods for class ContactPhone:

* `validate(self, phone)`: Validates the phone parameter using the US Phone Number pattern `###-###-####` and return true/false
* `set_info(self, value)`: Will validate the value parameter as a phone, set the phone number in self.phone attribute & store the object in the contact_list class variable; if validation is false, raise a `ValueError`
* `get_info()` - this will return the self.phone attribute

### Tips

* There are many ways to validate phone numbers or emails, but the most consistent and challenging method is to use the regular expression module.
* If you use the regex module, here is a pattern for phone numbers `regex = "^[2-9]\d{2}-\d{3}-\d{4}$"`

### Assistance at Rio Hondo

Need help? Contact the [Math, Science, & Engineering Center](https://www.riohondo.edu/mathematics-and-sciences/math-science-center/) for tutoring assistance. Any form of sharing or uploading of this assignment on external websites is strictly prohibited.

---

## Lab Questions

Do not provide code for any of the questions. You need to provide answers to each of the questions in normal written language answering each of the questions.

### Question 1

**In your child class `__init__()` method, what challenges did you need to overcome in order to be able to access the attributes and methods from the parent class?**

When defining the constructor for the child classes, I knew that I had to call the constructor method from the parent class. If any additional paramenter needed to be defined, I defined using self.attribute = parameter. 


### Question 2

**How does inheritance help reduce code in a program?**

Inheritance allows us to define multiple attributes and methods for a specific class that can then be used later on other classes without defining them again

### Question 3

**How can controlling when an exception is thrown be leveraged in your program code while using a class or object?**

The control over errors in the program allows it to stop immediately if anything happens

### Question 4

**What is the name of the concept for using the same method name in different child classes and why is it important?**

It is called overriding. It is important because it allows us to change the behavior of any specific method depending on what we want it to do on that specific class

---

## Bonus

In your class, add appropriate documentation strings to describe the class and each of the methods. Remember, comments are not documentation strings and will not count, you will need to research how to do this properly. A bonus up to +5 points is available for completing this.

Examples can be found at: [Docstrings in Python](https://www.datacamp.com/community/tutorials/docstrings-python)

## Rubric / Grading Criteria

See [Canvas](https://riohondo.instructure.com) for specific points breakdown on this assignment.

Grading is done via a combination of automatic grading in GitHub and manual testing by the instructor. Points may be deducted based on the following criteria:

* Must contain working Python code
  * Code follows all instructions listed above
  * Code is well structured, formatted, and commented
  * Code is able to be manually run without errors
  * Code uses concepts as covered in the current topic for the lab
  * Provided unit tests pass test with partial credit available for 1 or more passed tests
* More than 1 commit made by the student per GitHub Repo
* Tools such as the Measure of Software Similarity (MOSS) may be used to detect plagiarism

Points may still be deducted based on the grading criteria above even if the assignment passes the Auto Grading unit tests. **Creating code that is well structured, formatted, and commented cannot be tested automatically. So you can pass all your auto grading tests, but still lose points.**

## Testing & Auto Grading

Always try running your code in your local environment before submitting for grading and use the provided criteria for testing. Troubleshooting and debugging code is a process that you must learn to be an effective programmer as you will not be given test cases in real world programming, you will have to write them yourself. Find more information on testing on the code read the [TESTS.md](TESTS.md) file.

Auto Grading may use a combination of automated Input/Output testing, Unit Tests using pytest, or both via GitHub Classroom depending on the assignment. Scores in GitHub are not communicated to your Canvas lab assignment. The instructor must still manually grade each one then enter a grade.
