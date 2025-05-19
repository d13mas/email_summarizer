# tests/test_openai.py

import sys
import os

# Ensure the parent directory is in the path so "summarizer" can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from email_summarizer_pkg.summarizer import summarize_text

TEST_TEXT = """
Hi John,

I just wanted to follow up on the meeting we had yesterday regarding the new product launch timeline. 
After checking with the marketing and engineering teams, we believe we can move the release up by two weeks 
without impacting quality. I’ll sync with the QA team tomorrow to confirm test coverage and dependencies.

Let me know if you're aligned. We can finalize the comms plan by Friday.

Thanks,
Emily
"""

def test_openai_summary():
    summary = summarize_text(TEST_TEXT)
    assert isinstance(summary, str)
    assert len(summary) > 0
    print("\n--- Summary ---\n")
    print(summary)

if __name__ == "__main__":
    test_openai_summary()
