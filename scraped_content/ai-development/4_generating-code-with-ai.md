## Generating Code with AI

Prompt engineering has provided us with a solid foundation, teaching us to communicate effectively with AI models, guiding them to produce accurate and context-aware responses. Just answering questions is only the beginning, though, as these models can assist you in generating code, simplifying complex programming tasks, and even offering creative solutions to coding challenges.

On this page, we’ll see how generative AI, more specifically Azure OpenAI Service, can help us improve the code we write, solve challenges, and even teach us new coding skills. In order to achieve all this, writing effective prompts is crucial, so don’t forget to practice it often!

The Azure OpenAI service enables you to use large language models (LLMs) to generate content, including programming code. This functionality allows developers to generate and improve existing programming code in various languages to increase efficiency and understanding.

There are a few ways in which generative AI can be prompted to writing code, such as using natural language.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Generating Code with Natural Language
</edukamu-collapse-hidden-title>

One of the capabilities of Azure OpenAI models is to generate code from natural language prompts. Tasks can range from a simple one-line command to a full application. The AI models can also edit and update provided code or previous responses to complete the requested task.


### AI Models for Code Generation

Most of the language models available can help with code, with some performing better than others. In the base GPT-3 family, the standard text model (such as text-davinci-002) has a good base understanding of code. Codex (such as code-davinci-002) has expanded coding capabilities on top of the standard text model.

As new generations of models evolve, the base models drastically improve their performance and understanding of both language and code, which results in not needing specific Codex models. This improvement results in just a single model for more recent generations (such as gpt-35-turbo and gpt-4) that can be used for both natural language and code.

The examples in this section are using gpt-35-turbo.


### Writing Functions

Azure OpenAI models can create functions and apps in several languages by just describing what you want. For example, say you need an implementation of binary search but can't remember how it's done. Given the prompt write a function for binary search in python, you likely receive a response with the function and an explanation of the code.

```
code 
Sure, here's an example implementation of binary search algorithm in Python:

def binary_search(array, target):  
    low = 0  
    high = len(array) - 1  
  
    while low <= high:  
        mid = (low + high) // 2  
        if array[mid] == target:  
            return mid  
        elif array[mid] < target:  
            low = mid + 1  
        else:  
            high = mid - 1  
  
    return -1  

This function takes in two arguments - an array of integers and a target integer that we want to search for in the array. The function initializes two pointers - low and high - to the first and last indices of the array, respectively.

Inside the while loop, the function calculates the middle index using integer division (//). If the middle element is equal to the target, the function returns the index of the middle element. If the middle element is less than the target, we update the low pointer to mid + 1. Otherwise, we update the high pointer to mid - 1. We continue these steps until we find the target or the pointers cross each other (i.e., low > high).

If the target is not found in the array, the function returns -1.

Note that the binary search algorithm assumes that the input array is sorted in ascending order. If the array is not sorted, the algorithm may not return the correct result.
```

The request can go further than functions, and request a series of functions or an entire app. The response provides a good starting point for the task you're trying to achieve.

#### Changing Coding Language

If you have code in one language, but need it in another, Azure OpenAI can translate that for you. For example, say you have this print_squares function in **Python**.

```python
def print_squares(n):  
    for i in range(1, n+1):  
        print(i**2)   
```

If you provide that code, along with the prompt convert this code to **C#**, you likely get something similar to the following function.

```c#
public void PrintSquares(int n)  
{  
    for (int i = 1; i <= n; i++)  
    {  
        Console.WriteLine(i * i);  
    }  
}  
```

Notice the model understood the differences between how for loops and functions are defined in the different languages (including access modifiers in C#), and changed the code appropriately.

#### Understanding Unknown Code

Azure OpenAI models are helpful for understanding code that doesn't make sense, or may be in a language you aren't familiar with. For example, say you were given the following function (*in a fictitious coding language!*) and didn't know how to understand it.

``` 
code
fn qzplv(n: i32, m: i32) -> i32 {
    if n == 0 {
        return m + 1;
    } else if m == 0 {
        return qzplv(n - 1, 1);
    } else {
        return qzplv(n - 1, qzplv(n, m - 1));
    }
}
```

When provided to the model, along with the prompt could you explain what this code is doing, you get a response similar to the following:

```
code 
Sure, I'd be happy to explain what this code is doing!

This code is implementing the Ackermann function, which is a well-known mathematical function that 
grows very quickly in terms of computation time as its inputs increase. The function takes two integer 
arguments (n and m) and returns another integer.

Here's how the function works:
- If n is equal to 0, the function returns m + 1.
- If m is equal to 0, the function calls itself recursively with n - 1 and 1 as arguments.
- Otherwise, the function calls itself recursively with n - 1 and the result of calling itself with n 
and m - 1 as arguments.

The function is implemented in a way that is easy to understand and follow, but it has a very high 
computational complexity. In fact, it grows so quickly that it can't be computed for values of n and m 
greater than about 4 or 5.
```

Combining the explanation and translation into a language you're familiar with makes this functionality even more useful.

</edukamu-collapse>
<br>

As you can see, generative AI is quite capable at writing code based on the prompts with which you present it. It’s worth pointing out, though, that the content created by AI is almost never ready – you’ll most likely need to fine-tune and complement it with your own input. 


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Completing Code
</edukamu-collapse-hidden-title>

*(In the following examples, we’ll be using the C# programming language.)*

Azure OpenAI can assist developers in common software development tasks such as writing unit tests, completing partial code, commenting code, and generating documentation. Using AI assistance can enable developers to spend more time on complex programming and problem-solving tasks.


### 1. Completing Partial Code

Azure OpenAI models are capable of generating code based on comments, function names, and partially written code. The more context you can provide the model, the more accurate the response likely is.

For example, when given the following prompt:

```
prompt 
complete the following function    
"""    
// calculate the average of the numbers in an array, but only if they're even    
public 
```

The model takes the comments and start of the function definition, and complete it from whatever context it has.

```c#
// calculate the average of the even numbers in an array  
public double CalculateEvenAverage(int[] numbers) {  
    int total = 0;  
    int count = 0;  
    foreach (int number in numbers) {  
        if (number % 2 == 0) {  
            total += number;  
            count++;  
        }  
    }  
    if (count == 0) {  
        return 0;  // avoid division by zero  
    } else {  
        return (double) total / count;  
    }  
}
```

In this case, it was able to discern what we wanted due to a relatively simple and complete comment preceding the start of the function. With more complex functions or tasks, more context is required to get a useful response.

It's important to note that for some languages, like Python, the syntax is clear enough for the model to assume what language is desired. For syntactically similar languages like C# or Java, there's a higher likelihood that the model uses the wrong language. If that is the case, try specifying the language in the prompt or providing more code for context.

Similar functionality can be seen by providing partial code to the model, without any comments. Take the following prompt for example.

```
prompt 
complete the following code  
"""  
public int Func1(int n) {  
    if (n == 0) { 
```

The AI model does its best to complete the function with the most likely completion of the function.

```c#
public int Func1(int n) {  
    if (n == 0) {  
        return 1;  
    } else {  
        return n * Func1(n-1);  
    }  
}
```

The response likely also includes a natural language explanation of what that function is doing. In this case, it responded with a recursive implementation of the factorial function. However, the prompt could have also been the start of a Fibonacci function, which illustrates a case where we need more context in the prompt to better indicate what we want from the model.

Tools such as GitHub Copilot utilize OpenAI models to suggest code and function completions in a similar way to the above examples. GitHub Copilot is an excellent example of real-world usage of this functionality that uses built-in prompts and the context of the code you're writing to act as your paired programmer.

### 2. Writing Unit Tests

Azure OpenAI models can generate unit tests for functions you write to help make your code more robust. Take for example the binary search function.

```c#
public static int BinarySearch(int[] arr, int target)
{
    int left = 0;
    int right = arr.Length - 1;

    while (left <= right)
    {
        int mid = (left + right) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return -1;
}
```

Provide that function along with the prompt write three unit tests for this function, and you get a response similar to the following.

```c#
[Test]  
public void TestBinarySearch1()  
{  
    int[] arr = { 1, 2, 3, 4, 5 };  
    int target = 3;  
    int expected = 2;  
    int result = BinarySearch(arr, target);  
    Assert.AreEqual(expected, result);  
}  

[Test]  
public void TestBinarySearch2()  
{  
    int[] arr = { 10, 20, 30, 40, 50 };  
    int target = 35;  
    int expected = -1;  
    int result = BinarySearch(arr, target);  
    Assert.AreEqual(expected, result);  
}  

[Test]  
public void TestBinarySearch3()  
{  
    int[] arr = { 3, 6, 9, 12, 15 };  
    int target = 6;  
    int expected = 1;  
    int result = BinarySearch(arr, target);  
    Assert.AreEqual(expected, result);  
}  
```

This functionality is even more useful if you specify the cases you want included in your prompt, which reduces the time it takes for you to write unit tests for your code.

### 3. Adding Comments and Generating Documentation

To further improve your code, AI models can add comments and documentation for you. Take the following function as an example, which can be a little hard to understand when first reading it without any code comments.

<!-- **Tässä c# koodia, joka ei toimi koodiblokkina - Tehtävä esim. svgnä** -->
<edukamu-image url="/graphics/module4/2024-01-31-ai-models-and-comments.svg" alt="" style="">
<br>

Provide that function to the model, along with a prompt requesting that it add comments to the code, and you get a response similar to the following.

<!-- **Tässä c# koodia, joka ei toimi koodiblokkina - Tehtävä esim. svgnä** -->
<edukamu-image url="/graphics/module4/2024-01-31-ai-models-and-prompt-request.svg" alt="" style="">
<br>


Take it one step further, and request documentation for the function it just added comments to.

<!-- **Tässä c# koodia, joka ei toimi koodiblokkina - Tehtävä esim. svgnä** -->
<edukamu-image url="/graphics/module4/2024-01-31-ai-models-and-documentation-request.svg" alt="" style="">
<br>

</edukamu-collapse>
<br>

Like all people, generative AI can also make mistakes, which is why its input should be taken with a grain of salt. Generative AI can, however, also be helpful when it comes to finding and fixing the mistakes you might have made yourself while writing code. Here’s how.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Fixing Bugs and Improving the Code
</edukamu-collapse-hidden-title>

*(In the following examples, we’ll be using the C# programming language.)*

Developers sometimes can write code that mostly works, but could be improved by fixing bugs, syntax, performance, or modularity. Azure OpenAI models can help identify ways to improve and provide suggestions on how to write better code.


### 1. Fixing Bugs in Code

Azure OpenAI models can help fix bugs in code by analyzing the code and suggesting changes that can potentially fix the issue. This can help developers identify and resolve bugs faster and more efficiently.

For example, say you have the following function that isn't working for you.

```c#
public double CalculateAverage(int[] numbers)
{
    int total = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        int number = numbers[i];
        total += number;
    }
    double average = (double)total;
    rerun averave;
}
```

Provide that function to the model, along with the prompt Fix the bugs in this function, and you get a response with the fixed code and an explanation of what was fixed.

```c#
public double CalculateAverage(int[] numbers)
{
    int total = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        int number = numbers[i];
        total += number;
    }
    double average = (double)total / numbers.Length;
    return average;
}
```
<br>

>**Response**:
><br>
>AI <br>
>There were a few issues with the original code:
><br>
>1. The variable "average" was assigned the value of "total" instead of the actual average.
>2. There was a typo in the last line - "rerun" should be "return".
>3. The average was not actually calculated - the corrected code divides the total by the length of the "numbers" list to get the average.


### 2. Improving Code Performance

While code developers write may work, there might be a more efficient way to accomplish the task. Here's an example of a function that calculates the sum of the first n positive integers, possibly inefficiently:

```c#
public int SumOfN(int n)  
{  
    int result = 0;  
    for (int i = 1; i <= n; i++)  
    {  
        result += i;  
    }  
    return result;  
}  
```

This version works correctly, but its time complexity is O(n). When provided to the model, here's the response:

>AI<br> 
>We can improve this function it by using a mathematical formula instead.
><br>
>Here's the more efficient version:

```c#
public int SumOfN(int n)  
{  
    return n * (n + 1) / 2;  
}  
```

This version still returns the correct result, but its time complexity is now O(1), which makes it much more efficient.


### 3. Refactoring Inefficient Code

Better code is less prone to bugs and is easier to maintain, and the Azure OpenAI models can help guide developers on how to refactor their code.

Consider the following function.

```c#
public double CalculateTotalPrice(string item, int quantity)
{
    if (item == "apple")
    {
        return quantity * 0.5;
    }
    else if (item == "banana")
    {
        return quantity * 0.75;
    }
    else if (item == "orange")
    {
        return quantity * 0.6;
    }
    else
    {
        return 0;
    }
}
```

This code calculates the total price of a particular item based on its name and quantity. However, the code isn't modular and can be difficult to maintain. When provided to the model with the request to refactor it, here's the response:

<!-- **Tässä c# koodia, joka ei toimi koodiblokkina - Tehtävä esim. svgnä** -->
<edukamu-image url="/graphics/module4/2024-01-31-ai-models-and-refactor-request.svg" alt="" style="">
<br>

Along with the code, the model provides an explanation of the refactoring.

>AI<br> 
>In this refactored code, we've created an object called itemPrices that maps item names to their prices. We've also simplified the calculateTotalPrice function by using the itemPrices object to look up the price of the item, rather than using a series of if/else statements. This makes the code more modular and easier to maintain, and also reduces the risk of introducing bugs in the future.

</edukamu-collapse>
<br>

At this stage, you might already have some experience writing code. In fact, you could even be a professional programmer – or someone just getting started. Either way, generative AI can be extremely helpful when it comes to writing, improving, and correcting code, without even mentioning everything it offers for those who want to learn more.

Remember to experiment with generative AI as often as possible. You might for example write the following prompt: 

>“I’m experimenting with the C# programming language. I’m currently trying to write a basic calculator, but I’m struggling to get going. Could you point me to the right direction? How should I start writing code for my calculator? Only help me get started, please. Don’t write the whole code but tell me what to do. I have set up an IDE and a console application, so I’m ready to get going.”

To which the generative AI would provide a response akin to the following:

>“Certainly! Writing a basic calculator in C# is a great way to get familiar with fundamental programming concepts. Here's something you can do to get started:<br>
><br>
>1\. Write the Main Method, which is the entry point for your C# application. You'll write your logic here to accept user inputs and display results.<br>
>2\. Accept user inputs by using Console.ReadLine(). You'll need to accept at least two numbers and an operator (like +, -, *, /). Remember to convert the input strings to numbers (you can use int.Parse() or double.Parse() for this).<br>
>3\. Start implementing basic operations like Add that takes two numbers and returns their sum. Similarly, implement Subtract, Multiply, and Divide methods.<br>
><br>
>Here are a few tips to get you going. Here’s a pseudo-code outline to help visualize the structuce:

```
class Program
{
    static void Main(string[] args)
    {
        // Loop for continuous input
        while (true)
        {
            // Accept user inputs (numbers and operator)
            Console.WriteLine("Enter first number:");
            double num1 = double.Parse(Console.ReadLine());

            Console.WriteLine("Enter second number:");
            double num2 = double.Parse(Console.ReadLine());

            Console.WriteLine("Enter operator (+, -, *, /):");
            string operation = Console.ReadLine();

            // Process operation and display result
            try
            {
                double result = ProcessOperation(num1, num2, operation);
                Console.WriteLine("Result: " + result);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }

    static double ProcessOperation(double num1, double num2, string operation)
    {
        // Implement the logic to call Add, Subtract, Multiply, or Divide
        // based on the operation input
    }

    // Define methods for Add, Subtract, Multiply, Divide
}
```
> This structure should get you started. You can fill in the specific logic for each part. Remember, programming is often about experimenting and iterating, so don't hesitate to try different approaches and see what works best for you!

As the generative AI points out at the end, programming is about planning, experimenting, and iterating. The same applies for using generative AI – by experimenting with it, you’ll get better and better at it!

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Generating and Improving Code with Azure OpenAI Service
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll use Azure OpenAI models to generate and improve code. We’ll deploy an Azure OpenAI model and generate code in the playground and with the SDK.We’ll also get a chance to see how tasks can be completed with various code prompts, using AI to fix bugs.

(Microsoft provides this lab experience and related content for educational purposes. All presented information is owned by Microsoft and intended solely for learning about the covered products and services.)

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/generate-code-azure-openai/5-exercise?launch-lab=true" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
<br>

Please notice that you need to sign into your Microsoft account (personal or professional) in order to use the Lab environment. 

After signing in, you can launch the Lab environment by clicking on the button illustrated in the image below.

<edukamu-image url="/graphics/module1/lab-ohje.png" alt="Picture illustrating the lab button on Microsoft Learn." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The lab environment (Virtual Machine) will launch in a separate window. You’ll find detailed instructions on signing in, getting started, and completing the practice exercise on the right.

<edukamu-image url="/graphics/module1/lab-ohje-2.png" alt="Picture illustrating the lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Good luck!

</edukamu-collapse>
<br> -->

<edukamu-section class="slate-section slate-orange">
We’ve now explored Azure OpenAI Service from a variety of perspectives. We still have one important topic left to cover before completing the unit, though. 

Before moving forward, take some time to complete the following exercise.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Writing Code with Generative AI
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module4/generating-code-with-ai-question-scroll-1.yaml" id="culxdaimu4r3dvrz">
<br>

</edukamu-collapse>
<br>

Hopefully you’ve had the opportunity to play around with generative AI during this course! On the next page, we’ll take on an entirely different topic and make sure that we know how to implement (generative) AI responsibly and ethically.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
