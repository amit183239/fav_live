from django.conf import settings
from django.core import mail
from django.utils.html import strip_tags
import logging
logger = logging.getLogger('FavMedia')


def send(message, fail_silently=False):
    mailing_sequence = settings.EMAIL_CONFIG

    for mailer in mailing_sequence:
        logger.debug("SENDNG MAIL: trying to send the mail through %s", mailer)
        kwargs = {
            'host': getattr(settings, '%s_EMAIL_HOST' % mailer),
            'username': getattr(settings, '%s_EMAIL_HOST_USER' % mailer),
            'password': getattr(settings, '%s_EMAIL_HOST_PASSWORD' % mailer),
            'port': getattr(settings, '%s_EMAIL_PORT' % mailer),
            'use_tls': getattr(settings, '%s_EMAIL_USE_TLS' % mailer),
            'fail_silently': fail_silently
        }
        from_email = getattr(settings, '%s_DEFAULT_FROM_EMAIL' % mailer)
        message.from_email = "FavorableMedia <%s>" % from_email
        try:
            connection = mail.get_connection(**kwargs)
            connection.send_messages([message])
            logger.debug("SENDING MAIL: sent mails via '%s' mailer settings %s" % (mailer, kwargs))
            return True
        except:
            logger.exception(
                "SENDING MAIL: Unable to send using this '%s' mailer settings %s" % (mailer, kwargs))
            continue
    else:
        return False


def send_mail_lists(msg, fail_silently):
    if send(msg, fail_silently):
        logger.debug("Successfully sent email to %s" % ', '.join(msg.to))
        return msg
    else:
        logger.error('Failed to send email from SES to email %s, '
            'trying to send from default server' % ', '.join(msg.to))
        return False


def send_favmail(subject, message, to_email, is_html_message=False, attachments=None,
                bcc_email=None, content_subtype=None, headers=None, mimetype=None,
                fail_silently=False, attach_files=None, reply_to=None):
    """
    Try to send email with Amazon's SES, if failed, send from
    default server.
    inputs: subject - Email subject
            message - Email body
            is_html_message - True if message has html tags else False
            from_email - from email id
            to_email - list of to email ids
            attachment - Attachments if any
            attachment_name - Name of the attachment
            bcc_email - List of bcc email ids
            headers - Dict of email headers (default is None)

    output: True - If email is sent successfully
            False - If email sending failed (in both SES and gmail server)
    """
    if getattr(settings, 'TEST_MODE', False):
        test_ser_prefix = getattr(settings, 'EMAIL_SUBJECT_PREFIX', '[TEST BOX]')
        subject = test_ser_prefix + subject
    logger.info('Sending email to %s' % ', '.join(to_email))
    if isinstance(to_email, list) or isinstance(to_email, tuple):
        to_email = list(set(",".join([i for i in to_email if i]).split(',')))
        logger.debug('Email list continuing...')
    else:
        logger.error('To email id needs to be list not %s' % type(to_email))
        return False

    from_email = "customerservice@favorablemedia.com"
    if headers is None:
        headers = {}

    if is_html_message:
        text_content = strip_tags(message)
        msg = mail.EmailMultiAlternatives(subject, text_content, "favorablemedia <%s>" % from_email,
                                          to_email, headers=headers)
        msg.attach_alternative(message, 'text/html')
    else:
        msg = mail.EmailMessage(subject, message, "favorablemedia <%s>" % from_email, to_email,
                                headers=headers)

    if bcc_email:
        if type(bcc_email) != list:
            logger.error('bcc_email needs to be list not %s' % type(bcc_email))
            return False
        msg.bcc = bcc_email

    if content_subtype:
        msg.content_subtype = content_subtype

    # original_msg = msg

    if not send_mail_lists(msg, fail_silently=fail_silently):
        return False
    else:
        return msg

