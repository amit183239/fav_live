import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..//'))
APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..//'))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
app_basename = os.path.basename(APP_DIR)
os.environ['DJANGO_SETTINGS_MODULE']= app_basename + '.settings'
sys.path.append(path)
from soul.views import send_favmail


def main():
    message= '''<u></u>           <div style="width:100%;height:100%;margin:10px auto;padding:0;background-color:#ffffff;font-family:Arial,Tahoma,Verdana,sans-serif;font-weight:300;font-size:13px;text-align:center" bgcolor="#ffffff">
 <table class="m_7853648152281118894body-wrapper" style="max-width:600px" width="100%" cellspacing="0" cellpadding="0"> <tbody><tr> <td class="m_7853648152281118894header" style="width:10px;background-color:#027cd5" width="10" bgcolor="#027cd5">&nbsp;</td> <td class="m_7853648152281118894header" style="background-color:#027cd5;padding:0;margin:0" valign="middle" bgcolor="#027cd5" height="50" align="left"> <a style="text-decoration:none;outline:none;color:#ffffff;font-size:13px" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726055000&amp;usg=AFQjCNEaE0XSsQUXZrmI3ZOQDEiBa7O3ug"> <img src="https://ci4.googleusercontent.com/proxy/Z6SB0z5TRxaGgEQfNmSWcSfLWiW3atHAgnuk4DCGn2aREKmC0cau19Lx4xKjxX7fh5PcJbIr96GlEu8HOE89s949B80-fq-y7l-t3ICGELLjcK6W257brUzZiw=s0-d-e1-ft#http://img6a.flixcart.com/www/promos/new/20150709-142534-flipkart.png" alt="Flipkart.com" style="border:none" class="CToWUd" border="0" height="30"> </a> </td> <td class="m_7853648152281118894header" style="background-color:#027cd5;padding:0;margin:0" valign="middle" bgcolor="#027cd5" height="50" align="right"> <a style="text-decoration:none;outline:none;color:#ffffff;font-size:11px" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2Q0U7DMAxF_yUPe1rXdW3RqFTBn1TGSZhpHEdpOoEQ_45pxRM82ff42srNp7mboTkaNINxDBTM0aza30pJQ13bcPKB0gy5nFBYdc3yQsFVkNLyJCUDzi6PKBYleso8bVcmHR_WwhM7SyuPG9zAImtGN0q2Lm8AgRPQa9zRFKWQJ4RCEve5xOJiGTEQzgfkRHY_N-0Lf9c0AmmEtu8feuvPl765du4C0HSPbdc2Z_BtA1evtqi2SqvV-ia3-GzF_eRUhEWZtlwtd1QNKn-_orIr88dmelf8zwu-vgF6QFDyWAEAAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2Q0U7DMAxF_yUPe1rXdW3RqFTBn1TGSZhpHEdpOoEQ_45pxRM82ff42srNp7mboTkaNINxDBTM0aza30pJQ13bcPKB0gy5nFBYdc3yQsFVkNLyJCUDzi6PKBYleso8bVcmHR_WwhM7SyuPG9zAImtGN0q2Lm8AgRPQa9zRFKWQJ4RCEve5xOJiGTEQzgfkRHY_N-0Lf9c0AmmEtu8feuvPl765du4C0HSPbdc2Z_BtA1evtqi2SqvV-ia3-GzF_eRUhEWZtlwtd1QNKn-_orIr88dmelf8zwu-vgF6QFDyWAEAAA&amp;source=gmail&amp;ust=1498115726055000&amp;usg=AFQjCNGbLxbuIMn_XteXVmJELByxrFwEmA"> <img style="vertical-align:middle" alt="Download APP" src="https://ci5.googleusercontent.com/proxy/hS9JzJTA9y70XwZpM7nQq7HCCueE_fLN4VSjCulG6i4YZIaccgUKbdf3QPRso62TeaebhXxHaWbrExjLLioSgnHiwTscb2EFFMBSTOvLZYXETbb0X4ZqS3UTwKZ54d4=s0-d-e1-ft#http://img5a.flixcart.com/www/promos/new/20150722-131253-download-app.png" class="CToWUd" border="0" height="33">
 DOWNLOAD APP
 </a> </td> <td class="m_7853648152281118894header" style="width:10px;background-color:#027cd5" width="10" bgcolor="#027cd5">&nbsp;</td> </tr> </tbody></table> <table class="m_7853648152281118894body-wrapper" style="max-width:600px" width="100%" cellspacing="0" cellpadding="0"> <tbody><tr> <td class="m_7853648152281118894col" width="300" valign="top" align="center"> <table width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#006cb4"> <tbody><tr> <td style="border-bottom:solid 1px #ccc;padding:0;color:#ffffff" width="20%" valign="middle" height="35" align="right"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726055000&amp;usg=AFQjCNEaE0XSsQUXZrmI3ZOQDEiBa7O3ug"> <img src="https://ci4.googleusercontent.com/proxy/FMbOwsKWpm8b4k9W5w23IijKfJ37XdL5MYA-rMKD0IMx2PmsgClJkOI9DMQ2wlwsKLLpW5llbh3wr_WiNd82MrJVRnOHAPx1uGsJm5MWgbdkMPfGraumyA=s0-d-e1-ft#http://img6a.flixcart.com/www/promos/new/20150716-155048-track.png" alt="" class="CToWUd" border="0"> </a> </td> <td style="border-bottom:solid 1px #ccc;border-right:solid 1px #ccc;padding:0 0 0 5px" width="30%" valign="middle" height="35" align="left"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726055000&amp;usg=AFQjCNEaE0XSsQUXZrmI3ZOQDEiBa7O3ug"> <span style="font-size:11px;color:#e1e1e1;line-height:14px">TRACK</span><br> <span style="font-size:11px;color:#e1e1e1;line-height:14px">ORDER</span> </a> </td> <td style="border-bottom:solid 1px #ccc;padding:0;color:#ffffff" width="20%" valign="middle" height="35" align="right"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726055000&amp;usg=AFQjCNEaE0XSsQUXZrmI3ZOQDEiBa7O3ug"> <img src="https://ci5.googleusercontent.com/proxy/Gz7_oGPuMpw-hN6x5PBJkMNkNSbtEvScMYNK8V5tx0Rx-wxtzEHqPeyIJom2seHK1pM3yDC0UDzzj7XZqzqcj_CK0MChhzUMViNQaw7QOHoDmbvSDBVdGXw=s0-d-e1-ft#http://img6a.flixcart.com/www/promos/new/20150716-155048-cancel.png" alt="" class="CToWUd" border="0"> </a> </td> <td class="m_7853648152281118894no-right-border" style="border-bottom:solid 1px #ccc;border-right:solid 1px #ccc;padding:0 0 0 5px" width="30%" valign="middle" height="35" align="left"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"> <span style="font-size:11px;color:#e1e1e1;line-height:14px">CANCEL</span><br> <span style="font-size:11px;color:#e1e1e1;line-height:14px">ORDER</span> </a> </td> </tr> </tbody></table> </td> <td class="m_7853648152281118894col" width="300" valign="top" align="center"> <table width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#006cb4"> <tbody><tr> <td style="border-bottom:solid 1px #ccc;padding:0;color:#ffffff" width="20%" valign="middle" height="35" align="right"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"> <img src="https://ci4.googleusercontent.com/proxy/FpM4H0F7sVZEWNow7xB4JhpwBtBTqxxSkvDuW9m-pvRzcRcgRgA0uovtAtaVskq44sL9zdh26333hwslAM2zSWwrYbXnSeSlzkEII4zQ4G3Yd1FW9CoKLCk=s0-d-e1-ft#http://img5a.flixcart.com/www/promos/new/20150716-155048-return.png" alt="" class="CToWUd" border="0"> </a> </td> <td style="border-bottom:solid 1px #ccc;border-right:solid 1px #ccc;padding:0 0 0 5px" width="30%" valign="middle" height="35" align="left"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"> <span style="font-size:11px;color:#e1e1e1;white-space:nowrap;line-height:14px">FREE &amp; EASY</span><br><span style="font-size:11px;color:#e1e1e1;line-height:14px">RETURNS</span> </a> </td> <td style="border-bottom:solid 1px #ccc;padding:0;color:#ffffff" width="20%" valign="middle" height="35" align="right"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"> <img src="https://ci6.googleusercontent.com/proxy/YYTcZjY8fhJ_CVbhEcziNelIgq7hgBMyDzOI0iVs-XBdh4LfBYPkx8WxWYilD6pgvHWfOxfiG3JK3n8J9Hy4Kjuh5f7NaRS7kps3_gYRGR77swRj8Q=s0-d-e1-ft#http://img5a.flixcart.com/www/promos/new/20150716-155048-cs.png" alt="" class="CToWUd" border="0"> </a> </td> <td style="border-bottom:solid 1px #ccc;padding:0 0 0 5px" width="30%" valign="middle" height="35" align="left"> <a style="text-decoration:none;outline:none;display:block" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"> <span style="font-size:11px;color:#e1e1e1;line-height:14px">CUSTOMER</span><br> <span style="font-size:11px;color:#e1e1e1;line-height:14px">SUPPORT</span> </a> </td> </tr> </tbody></table> </td> </tr> </tbody></table>

<table class="m_7853648152281118894body-wrapper" style="max-width:600px;border-left:solid 1px #e6e6e6;border-right:solid 1px #e6e6e6" width="100%" cellspacing="0" cellpadding="0">  <tbody><tr> <td colspan="2" style="margin:0;padding:25px 20px 5px 25px" valign="top" bgcolor="FFFFFF" align="left"> <p style="padding:0 0 0 0;margin:0;font-size:16px"></p> <p style="padding:20px 0 0 0;margin:0;color:#565656;line-height:20px">
 </p><div><span style="font-family:Verdana">Hi amit maurya,</span><br><div><span style="font-family:Verdana"><br></span></div><div><span style="font-family:Verdana">We're writing to you about your recent order OD109160573422256000.</span></div><div><span style="font-family:Verdana"><br></span></div><div><span style="font-family:Verdana">We would like to let you know that due to an unforeseen technical issue, invoice for your order includes details for only 1 product. We've fixed the issue and you can now get an updated copy of your invoice by following these simple steps:</span></div><div><span style="font-family:Verdana"><br></span></div><div><span style="font-family:Verdana">1. Visit 'My Orders' on your Flipkart account- <a href="http://fkrt.it/bqWLi~NN" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://fkrt.it/bqWLi~NN&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGzbAPvl6Ag8Hc4H58hwKcZhZdJUQ">http://fkrt.it/bqWLi~NN</a></span></div><div><span style="font-family:Verdana">2. Click on the order for which you'd like the invoice and select the option 'Request Invoice' to get the invoice at your registered email ID</span></div><div><span style="font-family:Verdana"><br></span></div><div><span style="font-family:Verdana">Please be assured that instances like this are rare and we would like to thank you for your continued trust and understanding.</span></div><br><div><span style="font-family:Verdana">Thanks,</span></div><div><span style="font-family:Verdana">Flipkart</span></div><img style="width:1px;height:1px" src="https://ci4.googleusercontent.com/proxy/ThE6ZJLlFCb4K4-5a3sSMU49N8AT2NO636lzHaAlAyPY38Tng103LJnSrWK4AYYWz3BRQg_fDXBTArg1NHF5TsnkX0Qv_kheHWjYVOVQ349kKzZTCARr5ItlqUj8s80Fe_zBFzuqWhK4dwtCQ5x1_AML7uads2u_xYSbFPcZ50RENM9FliGuwEKdoHoZawjFo5uLbaVHX0qF4pbW05fc2BJJDm-VgwRG6xdOQU_EOG9EJor98A_nJ_Q1cstnFHuPG9Uxbhmz_NAnbLyuzTTw-xgWkL6Z0z8Xw4XlXlUxnAt8VNaSFYWr4V0LHTxMc9tVP7f3QOe5Aft1woyb8HQMT9qxL2vA5DhtaRLTJa-Dbcj7yEdyugtwfx9PlJU6yhscOtNNyzWq1pPr3Cf1Y9-XqcgRbZc8ydWyZD4_TJwtgg29s7nhQxwST9jXWF96Yqhih3MG7yZO6bVPiAyEuCZVOBwcroqle2YWdL71V5lVXqcFaC7lA1VZ00B-2bORvXE=s0-d-e1-ft#http://l.flipkart.com/t/open/H4sIAAAAAAAAAGVQy26DMBD8Fx9yCtjGuE2QUHvNV6CVbYibrG2BCYmq_nsXOOa289jRzv6yB2vkkRnWMIfg7-zIZpqvOaeGc4_DJ5T93T8NjLk0EfmyLHxzkgiDm3glpBa6EoWs60qrIo9gbmUKw9ecsUNn_YzttnFYiSnOo3FtHK0bN8IAJvBD2KkuxOx7byD7GHY9huxCbmNy4WAwebundbv_fYsqeKqgtP7QtheVlqfaVQCyPqtaSQG9knDqyRbItsZecCBkCf3Ea_i20a1ViTKZOBqxmB6GMBCkb6QbfaOwM-JrMz3XnPc7_v4BNAOxWl4BAAA" class="CToWUd"></div>
 <p></p> </td> </tr>  <tr> <td style="padding:15px 40px;margin:0;text-align:center;background-color:#f9f9f9" colspan="2" valign="top" bgcolor="F9F9F9" align="center"> <p style="padding:0;margin:0 0 7px 0"> <a style="text-decoration:none;color:#565656" href="http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA" title="Flipkart.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://l.flipkart.com/t/click/H4sIAAAAAAAAAG2PwY7CMAxE_yUHTpQS2q6gUgV_UllOshjqpCoOAq323zGtOO2e7HmZsSY_5m5auzZoWuMZaDBrk3U_i4xtWbphEwYarzDJBhOrLo9ZuGfvKHM3J1ZvcEt5Qt-lyflpBgg8An3HBfUxCQVCEEpxeU9RfJQOB8LrCnkkt5zrl8DfmDYjbVY1zVfjwnbX2H3tdwC2PlR1ZbcQKgv7oLaotkKn03lJ53hyyb_rK0JRpisXtzuqBpWfHxYuMz9n00PxPw1-X91yMfEvAQAA&amp;source=gmail&amp;ust=1498115726056000&amp;usg=AFQjCNGLkvYj1JIp2pAg0I7A-DovHtwV2A"><span style="color:#565656">Flipkart.com</span></a> </p> <p style="padding:10px 0 0 0;margin:0;border-top:solid 1px #cccccc;font-size:11px;color:#565656">
 24x7 Customer Support | Buyer Protection | Flexible Payment Options | Largest Collection
 </p> </td> </tr> </tbody></table>       <img style="width:1px;height:1px" src="https://ci4.googleusercontent.com/proxy/ThE6ZJLlFCb4K4-5a3sSMU49N8AT2NO636lzHaAlAyPY38Tng103LJnSrWK4AYYWz3BRQg_fDXBTArg1NHF5TsnkX0Qv_kheHWjYVOVQ349kKzZTCARr5ItlqUj8s80Fe_zBFzuqWhK4dwtCQ5x1_AML7uads2u_xYSbFPcZ50RENM9FliGuwEKdoHoZawjFo5uLbaVHX0qF4pbW05fc2BJJDm-VgwRG6xdOQU_EOG9EJor98A_nJ_Q1cstnFHuPG9Uxbhmz_NAnbLyuzTTw-xgWkL6Z0z8Xw4XlXlUxnAt8VNaSFYWr4V0LHTxMc9tVP7f3QOe5Aft1woyb8HQMT9qxL2vA5DhtaRLTJa-Dbcj7yEdyugtwfx9PlJU6yhscOtNNyzWq1pPr3Cf1Y9-XqcgRbZc8ydWyZD4_TJwtgg29s7nhQxwST9jXWF96Yqhih3MG7yZO6bVPiAyEuCZVOBwcroqle2YWdL71V5lVXqcFaC7lA1VZ00B-2bORvXE=s0-d-e1-ft#http://l.flipkart.com/t/open/H4sIAAAAAAAAAGVQy26DMBD8Fx9yCtjGuE2QUHvNV6CVbYibrG2BCYmq_nsXOOa289jRzv6yB2vkkRnWMIfg7-zIZpqvOaeGc4_DJ5T93T8NjLk0EfmyLHxzkgiDm3glpBa6EoWs60qrIo9gbmUKw9ecsUNn_YzttnFYiSnOo3FtHK0bN8IAJvBD2KkuxOx7byD7GHY9huxCbmNy4WAwebundbv_fYsqeKqgtP7QtheVlqfaVQCyPqtaSQG9knDqyRbItsZecCBkCf3Ea_i20a1ViTKZOBqxmB6GMBCkb6QbfaOwM-JrMz3XnPc7_v4BNAOxWl4BAAA" class="CToWUd"></div><div class="yj6qo"></div><div class="adL"> </div>'''

    send_favmail('Regarding your order [OD109160573422256000] with Flipkart.com!', message, ['amit.rebellion183@gmail.com'], is_html_message="True")

if __name__ == '__main__':
    main()

