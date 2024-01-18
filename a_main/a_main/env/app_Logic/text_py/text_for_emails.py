# contact forms emails -------------------------------------------------------------------------------

# auto reply to contact request

contact_request_body = """
Hi [USER_NAME],

Thank you for reaching out! I've received your message regarding [USER_SUBJECT], and I'll be sure to get back to you shortly.
I'm excited to discuss your photography needs and collaborate with you to create stunning visuals that capture your unique style.
In the meantime, please keep an eye on your inbox for my response. If you don't receive a follow-up email from me within 24 hours, 
please check your spam folder, just in case.

Looking forward to connecting with you soon!

Best regards,
Carly

SoftSubversion.com
[BODY]
"""


# contact form filled out 

contact_alart_body = '''
Subject: {SUBJECT]
From: [USER_EMAIL] - Name: [USER_NAME]
Message:
[BODY]'''
# client and project emails -------------------------------------------------------------------------------

# client requesing a new project 
project_request_notice_body = '''
Project Request!!!
From: [CLIENT_NAME] - ID#:[USER_ID]
Project Name: [PROJECT_NAME]
Requested Scope:  [SCOPE]
Requested date:  [DATE_SELECTED]
Requested Location type: [LOCATION]
Details [DETAILS]
'''

# notice to clinet of new comment on project request
request_post_comment = '''
Hey [USER_NAME],

A new comment has been posted on your project request for [PROJECT_NAME].

Commented:

        [COMMENT]

[LINK]
'''

send_invite_text = '''
Dear [CLIENT_NAME],

We're thrilled to extend an exclusive invitation for you to become a part of Soft Subversion's Online Studio, where you'll gain access to a world of captivating photography and personalized experiences.

To kickstart your journey with us and unlock the ability to submit project requests, you'll need to complete your registration by creating an account. To begin, please make note of your unique registration key: [REG_KEY]. Then, follow this link to register using your exclusive key:

[REG_URL]

Here's a brief overview of what you can anticipate from your Soft Subversion's Online Studio account:
Seamless Project Requests: You'll be able to submit project requests and directly collaborate with Carly to outline project details, ensuring your vision comes to life.

Private Proofing Gallery: Gain access to a private gallery where you can preview your photos for proofing purposes. Feel free to communicate directly with Carly to fine-tune your selections before finalization.

Easy Downloads and Printing: Once your final payment is processed, you'll have the convenience of downloading high-quality copies of your gallery and even ordering prints directly from Soft Subversion's Online Studio.

Should you encounter any questions or encounter any hiccups during the registration process, our dedicated support team is here to help. Reach out to us at support@softsubversion.com, and we'll guide you through any challenges you may face.
Thank you for choosing to embark on this creative journey with us at Soft Subversion's Online Studio. We look forward to helping you bring your photography and videography projects to life.

Warm regards,

Carley Brown
Photographer/Videographer 
Soft Subversion 
Website: softsubversion.com  
Email: Carly@softsubversion.com
'''

# Approved new project with deposit invoice 
new_project_and_invoice = '''

Dear [CLIENT_NAME],

I hope this message finds you well. I am excited to inform you that a new project has been approved and is now available in your Project Binder.

Project Details:
- Project Name: [PROJECT_NAME]
- [PAYMENT_TYPE] Invoice Number: [INVOICE_NUMBER]
- [PAYMENT_TYPE] Due Date: [DUE_DATE]
- [PAYMENT_TYPE] Amount Due: $[PAYMENT_DUE]

To ensure a smooth process, please take the following actions:
1. Click on the following link to view the project details: [PROJECT_LINK]
2. Review the project scope and details carefully.
3. Complete the attached questionnaire and upload it to your project details page.
4. You can follow this link to view and make a payment for the [PAYMENT_TYPE]: [PAYMENT_LINK]
5. Please make sure to complete the payment by the due date ([DUE_DATE]). Failure to do so may result in project cancellation.

If you have any questions or require further assistance, please don't hesitate to contact me.

Thank you for choosing Soft Subversion for your photography needs. I look forward to working with you on this exciting project!

Carley Brown
Photographer/Videographer 
Soft Subversion 
Website: softsubversion.com  
Email: Carly@softsubversion.com
'''

# Approved project without deposit invoice 
new_project_no_invoice = '''

Dear [CLIENT_NAME],

I hope this message finds you well. I am excited to inform you that a new project has been approved and is now available in your Project Binder.

Project Details:
- Project Name: [PROJECT_NAME]
- [PAYMENT_TYPE] Invoice Number: [INVOICE_NUMBER]
- [PAYMENT_TYPE] Due Date: [DUE_DATE]
- [PAYMENT_TYPE] Amount Due: $[PAYMENT_DUE]

To ensure a smooth process, please take the following actions:
1. Click on the following link to view the project details: [PROJECT_LINK]
2. Review the project scope and details carefully.
3. Complete the attached questionnaire and upload it to your project details page.
4. You can follow this link to view and make a payment for the [PAYMENT_TYPE]: [PAYMENT_LINK]
5. Please make sure to complete the payment by the due date ([DUE_DATE]). Failure to do so may result in project cancellation.

If you have any questions or require further assistance, please don't hesitate to contact me.

Thank you for choosing Soft Subversion for your photography needs. I look forward to working with you on this exciting project!

Carley Brown
Photographer/Videographer 
Soft Subversion 
Website: softsubversion.com  
Email: Carly@softsubversion.com
'''  

# Resend invoice 
resend_invoice = '''
Dear [CLIENT_NAME],
I hope this message finds you well. I wanted to provide you with a brief update on the status of your ongoing project, [PROJECT_NAME], and draw your attention to the pending invoice associated with it.
Invoice Summary:
	• Invoice Number: [INVOICE_NUMBER]
	• Due Date: [DUE_DATE]
	• Amount Due: $[PAYMENT_DUE]
To access and review the invoice details, please follow this link: [INVOICE_LINK].
Your prompt attention to the following is greatly appreciated:
	1. Review Invoice Details: Take a moment to thoroughly review the provided invoice details.
	2. Make Payment: Initiate the [PAYMENT_TYPE] payment by utilizing the secure payment link: [PAYMENT_LINK].
	3. Ensure Timely Payment: Please ensure the payment is completed on or before the due date ([DUE_DATE]) to avoid any potential disruptions to the project timeline.
Should you have any questions or require clarification regarding the invoice or any other project-related matter, feel free to reach out to me.
Thank you for your continued collaboration on this project. Your timely action on the invoice is crucial, and I appreciate your attention to this matter.
Best regards,
Carley Brown Photographer/Videographer 
Soft Subversion 
Website: softsubversion.com 
Email: Carly@softsubversion.com

'''