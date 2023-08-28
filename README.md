# Survey
Brief survey demo using Python, Flask, HTML templating, and Session storage 

<p>In this exercise, you will build a survey application.</p>
<p>It will ask the site visitor questions from a questionnaire,
one per screen, moving to the next question when they submit.</p>
<div class="section" id="step-zero-setup">
<h2>Step Zero: Setup</h2>
<p>Create a new virtual environment and activate it.</p>
<p>Install Flask and the Flask Debug Toolbar.</p>
<p>Make your project a Git repository, and add <cite>venv/</cite> and <cite>__pycache__</cite> to a new
<cite>.gitignore</cite> file for your repository.</p>
</div>
<div class="section" id="step-one-surveys">
<h2>Step One: Surveys</h2>
<p>We’ve provided a file, <cite>surveys.py</cite>, which includes classes for
<cite>Question</cite> (a single question on a survey, with a question,
a list of choices, and whether or not that question should allow
for comments) and <cite>Survey</cite> (a survey, which has a title,
instructions, and a list of <cite>Question</cite> objects).</p>
<p>For the main part of this exercise, you’ll only need to worry
about the <cite>satisfaction_survey</cite> survey in that file. It does
not include any questions that allow comments, so you can skip
that for now.</p>
<p>Play with the <cite>satisfaction_survey</cite> in ipython to get a feel
for how it works: it is an instance of the <cite>Survey</cite> class, and
its <cite>.questions</cite> attribute is a list of instances of the
<cite>Question</cite> class. You’ll need to understand this structure well,
so don’t move on until you feel comfortable with it.</p>
</div>
<div class="section" id="step-two-the-start-page">
<h2>Step Two: The Start Page</h2>
<p>For now, we’ll keep track of the user’s survey responses with a list in the
outermost scope in your <cite>app.py</cite>. To begin, initialize a variable called
<cite>responses</cite> to be an empty list. As people answer questions, you should store
their answers in this list.</p>
<p>For example, at the end of the survey, you should have in memory on the server
a list that looks like this:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="p">[</span><span class="s1">&#39;Yes&#39;</span><span class="p">,</span> <span class="s1">&#39;No&#39;</span><span class="p">,</span> <span class="s1">&#39;Less than $10,000&#39;</span><span class="p">,</span> <span class="s1">&#39;Yes&#39;</span><span class="p">]</span>
</pre></div>
</div>
<p>Next, let’s handle our first request. When the user goes to the root route,
render a page that shows the user the title of the survey, the instructions, and
a button to start the survey. The button should serve as a link that directs the
user to <cite>/questions/0</cite> (the next step will define that route).</p>
<p>Be sure to create a <cite>base.html</cite>  and use template inheritance!</p>
</div>
<div class="section" id="step-three-the-question-page">
<h2>Step Three: The Question Page</h2>
<p>Next, build a route that can handle questions — it should handle
URLs like <cite>/questions/0</cite> (the first question), <cite>/questions/1</cite>, and
so on.</p>
<p>When the user arrives at one of these pages, it should show a form asking the
current question, and listing the choices as radio buttons. Answering the
question should fire off a POST request to <cite>/answer</cite> with the answer the user
selected (we’ll handle this route next).</p>
</div>
<div class="section" id="step-four-handling-answers">
<h2>Step Four: Handling Answers</h2>
<p>When the user submits an answer, you should append this answer to your <cite>responses</cite>
list, and then <strong>redirect</strong> them to the next question.</p>
<p>The Flask Debug Toolbar will be <strong>very useful</strong> in looking at the submitted
form data.</p>
</div>
<div class="section" id="step-five-thank-the-user">
<h2>Step Five: Thank The User</h2>
<p>The customer satisfaction survey only has 4 questions, so once the user has
submitted four responses, there is no new question to task. Once the user has
answered all questions, rather than trying to send them to <cite>/questions/5</cite>,
redirect them to a simple “Thank You!” page.</p>
<div class="admonition note">
<p>Don’t Hardcode 5</p>
<p class="last">It’s possible that, in the future, this survey may include more than
four questions, so don’t hard-code 5 as the end. Do this in a way that
can handle any number of questions.</p>
</div>
</div>
<div class="section" id="step-six-protecting-questions">
<h2>Step Six: Protecting Questions</h2>
<p>Right now, your survey app might be buggy. Once people know the URL structure,
it’s possible for them to manually go to <cite>/questions/3</cite> before they’ve answered
questions 1 and 2. They could also try to go to a question id that doesn’t
exist, like <cite>/questions/7</cite>.</p>
<p>To fix this problem, you can modify your view function for the question show
page to look at the number in the URL and make sure it’s correct. If not, you
should redirect the user to the correct URL.</p>
<p>For example, if the user has answered one survey question, but then tries to
manually enter <cite>/questions/4</cite> in the URL bar, you should redirect them to
<cite>/questions/1</cite>.</p>
<p>Once they’ve answered all of the questions, trying to access any of the question
pages should redirect them to the thank you page.</p>
<div class="admonition note">
<p>Clearing the list</p>
<p>Once this functionality is built, there’s no way to reset the survey. Once
it’s complete, you can only see the start page and the thank you page.</p>
<p>By stopping and starting your server, you can complete the survey again (since
every time the server starts, Flask reads the <cite>app.py</cite> and re-initializes
<cite>responses</cite> to an empty list.</p>
<p class="last">We’ll fix this problem in Step Eight.</p>
</div>
</div>
<div class="section" id="step-seven-flash-messages">
<h2>Step Seven: Flash Messages</h2>
<p>Using <cite>flash</cite>, if the user does try to tinker with the URL and visit questions
out of order, flash a message telling them they’re trying to access an invalid
question as part of your redirect.</p>
</div>
<div class="section" id="step-eight-using-the-session">
<h2>Step Eight: Using the Session</h2>
<p>Storing answers in a list on the server has some problems. The biggest one is
that there’s only one list – if two people try to answer the survey at the same
time, they’ll be stepping on each others’ toes!</p>
<p>A better approach is to use the session to store response information, so
that’s what we’d like to do next. <strong>If you haven’t learned about the session yet, move on to step 9 and come back to this later.</strong></p>
<p>To begin, modify your start page so that clicking on the button fires off a POST
request to a new route that will set <cite>session[“responses”]</cite> to an empty list.
The view function should then redirect you to the start of the survey. (This
will also take care of the issue mentioned at the end of Step Six.) Then,
modify your code so that you reference the session when you’re trying to edit
the list of responses.</p>
<div class="admonition note">
<p>Why is this a POST request?</p>
<p class="last">Why are we changing “Start Survey” button from sending a GET request to
sending a POST request? Feel free to
ask for some support on this question.</p>
</div>
<div class="admonition note">
<p>Appending to a list in the session</p>
<p>When it comes time to modify the session, watch out. Normally, you can append
to a list like this:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fruits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;cherry&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>However, for a list stored in the session, you’ll need to rebind the
name in the session, like so:</p>
<div class="last highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fruits</span> <span class="o">=</span> <span class="n">session</span><span class="p">[</span><span class="s1">&#39;fruits&#39;</span><span class="p">]</span>
<span class="n">fruits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;cherry&quot;</span><span class="p">)</span>
<span class="n">session</span><span class="p">[</span><span class="s1">&#39;fruits&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">fruits</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="step-nine-celebrate">
<h2>Step Nine: Celebrate!</h2>
<p><strong>Good work!</strong></p>
</div>
</div>
