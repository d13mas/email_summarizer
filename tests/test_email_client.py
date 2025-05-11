import unittest
from unittest.mock import MagicMock, patch
import email
from email_summarizer import email_client

class TestEmailClient(unittest.TestCase):
    @patch('email_summarizer.email_client.IMAPClient')
    def test_connect_imap(self, mock_imap):
        # Setup mock
        mock_instance = mock_imap.return_value
        mock_instance.login.return_value = True
        mock_instance.select_folder.return_value = True

        # Call function
        client = email_client.connect_imap()

        # Assertions
        mock_imap.assert_called_with('imap.gmail.com', ssl=True)
        mock_instance.login.assert_called()
        mock_instance.select_folder.assert_called_with('INBOX', readonly=True)
        self.assertEqual(client, mock_instance)

    def test_parse_email_plain_text(self):
        # Create a mock email message with plain text
        msg = email.message.EmailMessage()
        msg.set_content("Hello, this is a test email.")
        msg_bytes = msg.as_bytes()
        msg_data = {b'RFC822': msg_bytes}

        result = email_client.parse_email(msg_data)
        self.assertEqual(result, "Hello, this is a test email.")

    def test_parse_email_multipart(self):
        # Create a multipart email with plain text and HTML parts
        msg = email.message.EmailMessage()
        msg.set_content("This is the plain text part.")
        msg.add_alternative("<html><body>This is HTML</body></html>", subtype='html')
        msg_bytes = msg.as_bytes()
        msg_data = {b'RFC822': msg_bytes}

        result = email_client.parse_email(msg_data)
        self.assertIn("This is the plain text part.", result)
        self.assertNotIn("This is HTML", result)

    @patch('email_summarizer.email_client.IMAPClient')
    def test_fetch_emails(self, mock_imap):
        # Setup
        mock_instance = mock_imap.return_value
        mock_instance.search.return_value = [1, 2]
        mock_instance.fetch.return_value = {
            1: {b'RFC822': b'Email1'},
            2: {b'RFC822': b'Email2'}
        }

        # Patch settings
        with patch('email_summarizer.email_client.settings') as mock_settings:
            mock_settings.search_subject = "Test"
            mock_settings.since_date = "2025-05-01"
            mock_settings.before_date = "2025-05-11"
            client = mock_instance
            emails = email_client.fetch_emails(client)
            self.assertEqual(len(emails), 2)
            mock_instance.search.assert_called()
            mock_instance.fetch.assert_called()

if __name__ == '__main__':
    unittest.main()
