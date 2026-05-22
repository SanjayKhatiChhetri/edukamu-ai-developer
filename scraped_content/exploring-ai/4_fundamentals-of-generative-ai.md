<edukamu-video content="/videos/devai-2-unit4-video.yaml"/>
<br>

## Fundamentals of Generative AI

Welcome to the fourth unit of this course!

So far, we’ve explored AI capabilities that, even individually, are quite amazing and something akin to science fiction. Combined, the tools have the potential to transform the lives of individuals, companies, or even whole societies. But there’s something even more revolutionary for us to discover in the world of artificial intelligence.

Imagine an artificial intelligence system not confined to following preset rules or mimicking human actions but one that can innovate, create, and even imagine. We’re talking about Generative AI, a technology that is pushing the boundaries of what machines can achieve.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Tip: Fascinated by AI?
</edukamu-collapse-hidden-title>

If you’re interested in generative AI, we highly suggest that you check out our Practical AI course. During this introductory course, you’ll learn everything you need to know about the basic operation models and use cases of generative AI – and you’ll also get to try out Microsoft’s state of the art services while doing so!

No previous knowledge or programming skills are required on the Practical AI course, and you can start studying immediately right here on Edukamu. Feel free to check it out!

<edukamu-button url="https://cs.edukamu.fi/practical-ai">Practical AI: Take me there!</edukamu-button>
<br>

The scope of the course is two European study credits (2 ECTS). In addition to the credits, you’ll also gain an official certificate for completing the course as well as a digital badge to boost up your LinkedIn profile.

Practical AI is an independent course which is not tied to any micro degree. In practice, this means that you can complete it any time you like.

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### YRITYKSEN NIMI: Career in the Cloud
</edukamu-collapse-hidden-title>
Hello, future data professional! At YRITYS, we work with services like Microsoft Azure every day, solving problems and improving the business of our clients and customers.

All over the world, companies like ours are shaping the future with intelligent features. From programming to management, governance to cybersecurity, all fields are equally important when developing the next technological revolutions.

On the following video, Nimi Niminen, Ammattinimike at Yritys talks about his/her job and career in the world of data.

VIDEO

If you’re interested in working with us, you can share your details with us after reaching the end of the course! Now, do your best on the course!

</edukamu-collapse>
<br> -->

At its core, Generative AI involves machines that don't just process data; they generate new, unique content. You too might have already experienced the power of generative AI – be it chatting with an incredibly human-like bot, creating new music, or turning your personal photos into Picasso-styled paintings by using text-based commands.

No longer confined to the binary world of 0s and 1s, Generative AI introduces an element of unpredictability, injecting a touch of innovation into the digital landscape.

And all this is, naturally, available in Microsoft Azure.

Before digging deeper, let’s spend a few moments getting familiar with generative AI. We’ll explore a few key concepts, namely 1) the basis of generative AI itself and 2) large language models.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Introduction to Generative AI
</edukamu-collapse-hidden-title>

Artificial Intelligence (AI) imitates human behavior by using machine learning to interact with the environment and execute tasks without explicit directions on what to output.

Generative AI describes a category of capabilities within AI that create original content. People typically interact with generative AI that has been built into chat applications. One popular example of such an application is ChatGPT, a chatbot created by OpenAI, an AI research company that partners closely with Microsoft.

Generative AI applications take in natural language input, and return appropriate responses in a variety of formats such as natural language, images, or code.

### Natural Language Generation

To generate a natural language response, you might submit a request such as "*Give me three ideas for a healthy breakfast including peppers.*"

A generative AI application might respond to such a request like this:

*OK, here are three healthy breakfasts that include peppers:*
1. *Egg and Pepper Scramble: Dice up some bell peppers and sauté them in a pan until they're slightly softened. Then, add in some beaten eggs and scramble everything together. Serve with whole-grain toast for a nutritious breakfast.*
2. *Pepper and Avocado Toast: Toast a slice of whole-grain bread and top it with sliced bell peppers, mashed avocado, and a sprinkle of salt and pepper. This is a great way to get some healthy fats from the avocado along with the vitamin C from the peppers.*
3. *Breakfast Burrito with Peppers: Sauté some diced bell peppers, onions, and scrambled eggs together in a pan. Then, spoon the mixture onto a whole-grain tortilla and top with some salsa or hot sauce. Roll it up and enjoy a satisfying and nutritious breakfast.*

### Image Generation

Some generative AI applications can interpret a natural language request and generate an appropriate image. For example, you might submit a request like "*Create an image of an elephant eating a burger*".

A generative AI application could then return an original new image based on the description you provided, like this:

<edukamu-image url="/graphics/module4/generated-image.png" alt="Illustration of an elephant eating a burger."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 


### Code Generation

Some generative AI applications are designed to help software developers write code. For example, you could submit a request like "*Show me how to code a game of tic-tac-toe with Python*" and generate the following response:

*Sure, here's some basic code for a Tic-Tac-Toe game in Python:*

```python
board = [' ' for x in range(9)]  
  
def print_board():  
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])  
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])  
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])  
    print()  
    print(row1)  
    print(row2)  
    print(row3)  
    print()  
  
def player_move(icon):  
    if icon == 'X':  
        number = 1  
    elif icon == 'O':  
        number = 2  
    print('Your turn player {}'.format(number))  
    choice = int(input('Enter your move (1-9): ').strip())  
    if board[choice - 1] == ' ':  
        board[choice - 1] = icon  
    else:  
        print()  
        print('That space is taken!')  
  
def is_victory(icon):  
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \  
       (board[3] == icon and board[4] == icon and board[5] == icon) or \  
       (board[6] == icon and board[7] == icon and board[8] == icon) or \  
       (board[0] == icon and board[3] == icon and board[6] == icon) or \  
       (board[1] == icon and board[4] == icon and board[7] == icon) or \  
       (board[2] == icon and board[5] == icon and board[8] == icon) or \  
       (board[0] == icon and board[4] == icon and board[8] == icon) or \  
       (board[2] == icon and board[4] == icon and board[6] == icon):  
        return True  
    else:  
        return False  
  
def is_draw():  
    if ' ' not in board:  
        return True  
    else:  
        return False  
  
while True:  
    print_board()  
    player_move('X')  
    print_board()  
    if is_victory('X'):  
        print('X Wins! Congratulations!')  
        break  
    elif is_draw():  
        print('The game is a draw!')  
        break  
    player_move('O')  
    if is_victory('O'):  
        print_board()  
        print('O Wins! Congratulations!')  
        break  
    elif is_draw():  
        print('The game is a draw!')  
        break  
```

*This is just a basic implementation of the game, and can be improved upon with additional features such as error handling and input validation.*

In addition to text, images, and code, generative AI is also able to produce fresh music or art, for instance, and publicly available services are already being used.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Introduction to Large Language Models
</edukamu-collapse-hidden-title>

Generative AI applications are powered by *large language models* (LLMs), which are a specialized type of machine learning model that you can use to perform *natural language processing* (NLP) tasks, including:
* Determining *sentiment* or otherwise classifying natural language text.
* Summarizing text.
* Comparing multiple text sources for semantic similarity.
* Generating new natural language.

While the mathematical principles behind these LLMs can be complex, a basic understanding of the architecture used to implement them can help you gain a conceptual understanding of how they work.

### Transformer Models

Machine learning models for natural language processing have evolved over many years. Today's cutting-edge large language models are based on the *transformer* architecture, which builds on and extends some techniques that have been proven successful in modeling *vocabularies* to support NLP tasks - and in particular in generating language. Transformer models are trained with large volumes of text, enabling them to represent the semantic relationships between words and use those relationships to determine probable sequences of text that make sense. Transformer models with a large enough vocabulary are capable of generating language responses that are tough to distinguish from human responses.

Transformer model architecture consists of two components, or *blocks*:
* An *encoder* block that creates semantic representations of the training vocabulary.
* A *decoder* block that generates new language sequences.

In practice, the specific implementations of the architecture vary – for example, the Bidirectional Encoder Representations from Transformers (BERT) model developed by Google to support their search engine uses only the encoder block, while the Generative Pretrained Transformer (GPT) model developed by OpenAI uses only the decoder block.

While a complete explanation of every aspect of transformer models is beyond the scope of this course, an explanation of some of the key elements in a transformer can help you get a sense for how they support generative AI.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Keep in mind that today’s most advanced LLMs are based on the so-called transformer architecture.  This is an important piece of information to remember as we explore the rest of this page.

Large language models – or in this case, transformer models – employ a variety of different tools and processes as they aim to fulfill every request, or command, given by the user. These include concepts like tokenization, which you’ve already heard of before, embeddings, and attention.

Let’s review these core concepts one by one.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Tokenization in Transformer Models
</edukamu-collapse-hidden-title>

The first step in training a transformer model is to decompose the training text into *tokens* - in other words, identify each unique text value. For the sake of simplicity, you can think of each distinct word in the training text as a token (though in reality, tokens can be generated for partial words, or combinations of words and punctuation).

For example, consider the following sentence:

*I heard a dog bark loudly at a cat*

To tokenize this text, you can identify each discrete word and assign token IDs to them. For example:
* I (1)
* heard (2)
* a (3)
* dog (4)
* bark (5)
* loudly (6)
* at (7)
* (*"a" is already tokenized as 3*)
* cat (8)

The sentence can now be represented with the tokens: [*1 2 3 4 5 6 7 3 8*]. Similarly, the sentence "I heard a cat" could be represented as [*1 2 3 8*].

As you continue to train the model, each new token in the training text is added to the vocabulary with appropriate token IDs:
* meow (9)
* skateboard (10)
* *and so on...*

With a sufficiently large set of training text, a vocabulary of many thousands of tokens could be compiled.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Embeddings in Transformer Models
</edukamu-collapse-hidden-title>

While it may be convenient to represent tokens as simple IDs - essentially creating an index for all the words in the vocabulary, they don't tell us anything about the meaning of the words, or the relationships between them. To create a vocabulary that encapsulates semantic relationships between the tokens, we define contextual vectors, known as *embeddings*, for them.

Vectors are multi-valued numeric representations of information, for example [10, 3, 1] in which each numeric element represents a particular attribute of the information. For language tokens, each element of a token's vector represents some semantic attribute of the token. The specific categories for the elements of the vectors in a language model are determined during training based on how commonly words are used together or in similar contexts.

It can be useful to think of the elements in a token embedding vector as *coordinates* in multidimensional space, so that each token occupies a specific "location." The closer tokens are to one another along a particular dimension, the more semantically related they are.

In other words, related words are grouped closer together. As a simple example, suppose the embeddings for our tokens consist of vectors with three elements, for example:
* 4 ("dog"): [10.3.2]
* 5 ("bark"): [10,2,2]
* 8 ("cat"): [10,3,1]
* 9 ("meow"): [10,2,1]
* 10 ("skateboard"): [3,3,1]

We can plot the location of tokens based on these vectors in three-dimensional space, like this:

<edukamu-image url="/graphics/module4/embed-example.png" alt="Diagram of token vectors plotted in three-dimensional space."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The locations of the tokens in the embeddings space include some information about how closely the tokens are related to one another. For example, the token for "dog" is close to "cat" and also to "bark." The tokens for "cat" and "bark" are close to "meow." The token for "skateboard" is further away from the other tokens.

There are multiple ways you can calculate appropriate embeddings for a given set of tokens, including language modeling algorithms like Word2Vec or the encoder block in a transformer model.

**Note**: The previous example shows a simple example model in which each embedding has only three dimensions. Real language models have many more dimensions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Attention in Transformer Models
</edukamu-collapse-hidden-title>

The *encoder* and *decoder* blocks in a transformer model include multiple layers that form the neural network for the model. We don't need to go into the details of all these layers, but it's useful to consider one of the types of layers that is used in both blocks: *attention* layers.

Attention is a technique used to examine a sequence of text tokens and try to quantify the strength of the relationships between them. In particular, *self-attention* involves considering how other tokens around one particular token influence that token's meaning.

In an encoder block, attention is used to examine each token in context, and determine an appropriate encoding for its vector embedding. The vector values are based on the relationship between the token and other tokens with which it frequently appears. This contextualized approach means that the same word might have multiple embeddings depending on the context in which it's used - for example "the bark of a tree" means something different to "I heard a dog bark."

In a decoder block, attention layers are used to predict the next token in a sequence. For each token generated, the model has an attention layer that takes into account the sequence of tokens up to that point. The model considers which of the tokens are the most influential when considering what the next token should be. For example, given the sequence “I heard a dog,” the attention layer might assign greater weight to the tokens “heard” and “dog” when considering the next word in the sequence:

**I heard a dog [bark]**

Remember that the attention layer is working with numeric vector representations of the tokens, not the actual text. In a decoder, the process starts with a sequence of token embeddings representing the text to be completed. The first thing that happens is that another *positional encoding* layer adds a value to each embedding to indicate its position in the sequence:
* \[**1**,5,6,2] (I)
* \[**2**,9,3,1] (heard)
* \[**3**,1,1,2] (a)
* \[**4**,10,3,2] (dog)

During training, the goal is to predict the vector for the final token in the sequence based on the preceding tokens. The attention layer assigns a numeric *weight* to each token in the sequence so far. It uses that value to perform a calculation on the weighted vectors that produces an *attention score* that can be used to calculate a possible vector for the next token. In practice, a technique called *multi-head attention* uses different elements of the embeddings to calculate multiple attention scores. A neural network is then used to evaluate all possible tokens to determine the most probable token with which to continue the sequence.

The process continues iteratively for each token in the sequence, with the output sequence so far being used regressively as the input for the next iteration – essentially building the output one token at a time.

The following animation shows a simplified representation of how this works – in reality, the calculations performed by the attention layer are more complex; but the principles can be simplified as shown:

<edukamu-image url="/graphics/module4/attention.gif" alt="Animation showing an attention layer assigning weights to tokens and predicting the next one."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

A sequence of token embeddings is fed into the attention layer. Each token is represented as a vector of numeric values.
1. The goal in a decoder is to predict the next token in the sequence, which will also be a vector that aligns to an embedding in the model’s vocabulary.
2. The attention layer evaluates the sequence so far and assigns weights to each token to represent their relative influence on the next token.
3. The weights can be used to compute a new vector for the next token with an attention score. Multi-head attention uses different elements in the embeddings to calculate multiple alternative tokens.
4. A fully connected neural network uses the scores in the calculated vectors to predict the most probable token from the entire vocabulary.
5. The predicted output is appended to the sequence so far, which is used as the input for the next iteration.

During training, the actual sequence of tokens is known – we just mask the ones that come later in the sequence than the token position currently being considered. As in any neural network, the predicted value for the token vector is compared to the actual value of the next vector in the sequence, and the loss is calculated.

The weights are then incrementally adjusted to reduce the loss and improve the model. When used for inferencing (predicting a new sequence of tokens), the trained attention layer applies weights that predict the most probable token in the model’s vocabulary that is semantically aligned to the sequence so far.

What all of this means, is that a transformer model such as GPT-4 (the model behind ChatGPT and Bing) is designed to take in a text input (called a prompt) and generate a syntactically correct output (called a completion). In effect, the “magic” of the model is that it has the ability to string a coherent sentence together.

This ability doesn't imply any “knowledge” or “intelligence” on the part of the model; just a large vocabulary and the ability to generate meaningful sequences of words. What makes a large language model like GPT-4 so powerful however, is the sheer volume of data with which it has been trained (public and licensed data from the Internet) and the complexity of the network. This enables the model to generate completions that are based on the relationships between words in the vocabulary on which the model was trained; often generating output that is indistinguishable from a human response to the same prompt.

</edukamu-collapse>
<br>


As you can see, large language models powering generative AI are not that complicated on the surface level. When given a little attention, the core processes are understandable.

Now that we’ve covered the basics, it’s time to start exploring Microsoft Azure from the perspective of generative AI. First, though, it’s time for an exercise!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to Generative AI
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module4/fundamentals-of-generative-ai-question-scroll.yaml" id="8pf9f53df2n1vcl0">
<br>

</edukamu-collapse>
<br>


Before you move on, here’s a little something for you to ponder: Is the content generated by generative AI actually new? Either way, why would you need to think about that, you might say. You’ll find out on the next page.

On the next page, we’ll also get acquainted with Azure OpenAI and something called copilots.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
