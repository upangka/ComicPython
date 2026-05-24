"""
L02_using_gemini_in_a_native_way.py

This module demonstrates how to use Google's Gemini chat models in a native way.
It covers the initialization of Gemini models using the appropriate client libraries,
configuring API endpoints with proper authentication, and setting model-specific parameters.
This serves as an example for integrating Google's Gemini language models into Python applications.
"""

from google import genai
from google.genai import types


client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="low",
            include_thoughts=True),
    ),
)

print(type(response))
print('━' * 100)
print(response)
print('━' * 100)
print(response.text)
print('━' * 100)

# print all thoughts
for part in response.candidates[0].content.parts:
    if part.thought:
        print(part.text)

"""
<class 'google.genai.types.GenerateContentResponse'>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
sdk_http_response=HttpResponse(
  headers=<dict len=12>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text=\"""**My Thought Process on Summarizing AI's Functionality Concisely**

Okay, so the prompt is asking for a ridiculously short explanation of how AI works. "In a few words," it says. Right, let's break this down. First, I need to understand the core elements: input, pattern recognition, learning, and output – the whole data-in, decision-out thing. We're essentially talking about finding patterns within data to drive the system’s actions.

Initially, I jotted down a few drafts. "AI learns from huge amounts of data to find patterns and make predictions" – bit wordy, needs to be tighter. Then, "Training on data, finding patterns, and making predictions" – accurate, but could be cleaner. "AI learns patterns from data to make decisions" – now we're getting somewhere, nice and concise. Then, I went super short: "It finds patterns in data to make predictions."

I considered "AI finds patterns in data to make predictions and decisions," but it felt a little clunky. I even toyed with "It analyzes vast data, finds patterns, and makes smart predictions," but I don't want to get into marketing speak. The simplest, most accurate version is the best: "AI learns patterns from data to make decisions." That's the core of it, distilled to its essence, covering the heart of machine learning. That'll work.


\""",
        thought=True
      ),
      Part(
        text='AI **learns patterns from data** to make decisions and predictions.',
        thought_signature=b'\x12\xff\t\n\xfc\t\x01\x0c9\xd6\xc7Hz\x0c\x08+\xaf\xb8/\xb2\x07\x9c\xaa\x86\xedf\x14\x18G\xd0\xda\x94q\x0f\x00\x1d\xabt\x84\xa8>fT\x1a\x9a)"\x1b<\xf1S\xeb[UC9\xf8p\xa5\x9e\xc1\xb14\xd2\x13\xc8e|\x88>\x0fxV<5\x8b\xac\xb9\x86\xdf\\^\xb2\xd1)&,\xa9\xc4\x11\xba\xfc\xf7J\xb8\xaf\xcb...'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-3.5-flash' prompt_feedback=None response_id='lcQSaoi4AvmlkdUP_6HEwQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=14,
  prompt_token_count=10,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=10
    ),
  ],
  thoughts_token_count=324,
  total_token_count=348
) model_status=None automatic_function_calling_history=[] parsed=None
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI **learns patterns from data** to make decisions and predictions.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**My Thought Process on Summarizing AI's Functionality Concisely**

Okay, so the prompt is asking for a ridiculously short explanation of how AI works. "In a few words," it says. Right, let's break this down. First, I need to understand the core elements: input, pattern recognition, learning, and output – the whole data-in, decision-out thing. We're essentially talking about finding patterns within data to drive the system’s actions.

Initially, I jotted down a few drafts. "AI learns from huge amounts of data to find patterns and make predictions" – bit wordy, needs to be tighter. Then, "Training on data, finding patterns, and making predictions" – accurate, but could be cleaner. "AI learns patterns from data to make decisions" – now we're getting somewhere, nice and concise. Then, I went super short: "It finds patterns in data to make predictions."

I considered "AI finds patterns in data to make predictions and decisions," but it felt a little clunky. I even toyed with "It analyzes vast data, finds patterns, and makes smart predictions," but I don't want to get into marketing speak. The simplest, most accurate version is the best: "AI learns patterns from data to make decisions." That's the core of it, distilled to its essence, covering the heart of machine learning. That'll work.
"""