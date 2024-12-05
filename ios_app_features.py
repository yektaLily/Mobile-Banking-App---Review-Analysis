import numpy as np 
import pandas as pd 
import time
from datetime import datetime


data_ios_appInfo = [
    {
        'CIBC':{
            'date_collection': datetime.now().strftime("%Y-%m-%d"), #datetime 
            'appname': "CIBC Mobile Banking",
            'category': "Finance",
            'headline': "Everyday banking on the go", 
            'theme_color': "red",
            'name_in_icon': 1, #binary, 1: includes name, 0: does not 
            'chart_rank': 4,  #rank on chart on date this was collected
            'avg_rating': 4.2, 
            'num_ratings': 21000,
            'age_min': 4, #minimum age for use
            'price': "free",
            'num_pictures_iphone': 8, #number of screenshots of the app UI uploaded by developer for iPhone 
            'num_pictures_ipad': 3, #number of screenshots of the app UI uploaded by developer for iPad 
            'num_pictures_watch': 4, #number of screenshots of the app UI uploaded by developer for Apple Watch 
            'developer': 'CIBC',
            'language': ['EN','FR'], 
            'size': 140.7, #megabytes
            'device_compatible': ['iphone', 'ipad', 'apple watch'], 
            'most_frequent_stars': "5",
            'second_most_frequent_stars': "4",
            'third_most_frequent_stars': "1",
            'update_info': '2024-09-26', #Sep 26, 2024
            'version': '10.57.3', 
            'latest_version_rate': 3.72,
            'latest_version_numRating': 278,
            'data_gathered': ['purchases', 'search history', 'usage data', 'location', 'sensitive info', 'identifiers'], #what data the app collects
            'apple_watch': 1,    #supports apple watch 
            'apple_wallet': 1, #supports apple wallet
            'youmightlike': ['Neo Financial', 'Borrowel: Credit Report', 'TD Insurance', 'Western Union Send Money', 'MBNA Canada', 'PC Financial Mobile'],
            'summary': """FIND IMPORTANT DISCLOSURES BELOW. The CIBC Mobile Banking App has received the highest ranking in customer satisfaction in Canada, according to a 2021 study from J.D. Power. We’re always striving to make our app do more for you.
            • Securely access your accounts with your fingerprint, face ID or password.
            • Apply for bank accounts or credit cards and view your application status in real time.
            • Get a snapshot of all your accounts in the same place, anytime.
            • Use Apple Pay/Google Pay or Samsung Pay at payment terminals.
            • Set up instant, post-dated or recurring payments.
            • Deposit cheques in a flash - all you need is to take a picture with your phone.
            • Send and receive money instantly with Interac e-Transfer.
            • Quickly search for branches, banking hours, bank machines and mortgage advisors near you.
            • Receive your free Equifax credit score directly in the app, without affecting your score.
            • Our Travel Tools feature a currency converter, helpful tips and emergency numbers for while you’re away.
            • Our Virtual Assistant is available 24/7 to answer your banking questions and is able to perform everyday banking transactions on your behalf.
            LANGUAGES:
            Supports English and French
            PRIVACY:
            Your privacy and security comes first. Learn more about how CIBC is committed to protecting you by visiting https://www.cibc.com/en/privacy-security.html.
            LEGAL:
            By downloading the CIBC Mobile Banking App you consent to the installation of this App and to any future updates or upgrades which may be automatically installed depending upon your device or operating system’s default settings or the settings you have selected. The app (including any updates or upgrades) may: (i) cause your device to automatically communicate with our servers to deliver the features and functionality described in the app description or through new features as they are introduced, and to record usage metrics; (ii) collect, use and disclose personal information as set out in our Privacy Policy; and (ii) affect preferences or data stored on your device. You can withdraw your consent at any time by uninstalling this App. For assistance, contact CIBC at the mailing address below.
            CONTACT:
            For your banking questions, please visit: https://www.cibc.com/en/contact-us.html.
            Telephone Banking: 1-800-465-2422.
            Address: CIBC Head Office, 81 Bay Street, CIBC Square, Toronto, Ontario, Canada M5J 0E7. 
            Website: http://www.cibc.com""",
            'url_link': "https://apps.apple.com/ca/app/cibc-mobile-banking/id351448953"
        },
        'TD':{
            'date_collection': datetime.now().strftime("%Y-%m-%d"), #datetime 
            'appname': "TD Canada",
            'category': "Finance",
            'headline': "Bank on the go with the TD app", 
            'theme_color': "green",
            'name_in_icon': 1, #binary, 1: includes name, 0: does not 
            'chart_rank': 5,  #rank on chart on date this was collected
            'avg_rating': 4.5, 
            'num_ratings': 79200,
            'age_min': 4, #minimum age for use
            'price': "free",
            'num_pictures_iphone': 10, #number of screenshots of the app UI uploaded by developer for iPhone 
            'num_pictures_ipad': 10, #number of screenshots of the app UI uploaded by developer for iPad 
            'num_pictures_watch': 4, #number of screenshots of the app UI uploaded by developer for Apple Watch 
            'developer': 'TD',
            'language': ['EN','FR','SCH','TCH'], #SCH: Simplified Chinese, TCH: Traditional Chinese 
            'size': 328.2, #megabytes
            'device_compatible': ['iphone', 'ipad', 'apple watch'], 
            'most_frequent_stars': "5",
            'second_most_frequent_stars': "4",
            'third_most_frequent_stars': "1",
            'update_info': '2024-10-21', #Oct 21, 2024
            'version': '24.09', 
            'latest_version_rate': 4.6,
            'latest_version_numRating': 1153,
            'data_gathered': ['usage data', 'location', 'diagnostics', 'identifiers'], #what data the app collects
            'apple_watch': 1,    #supports apple watch 
            'apple_wallet': 1, #supports apple wallet
            'youmightlike': ['TD Insurance', 'Western Union Send Money', 'Borrowel: Credit Report', 'KOHO: Award-winning Money App', 'PC Financial Mobile', 'Capital One Canada'],
            'summary': """Get ready to bank here, there, everywhere with the TD app.
                The TD app for iOS provides quick, easy, secure access to your TD chequing, savings, credit, and investment accounts.
                MOBILE BANKING:
                • Check account balances and transaction history.
                • Make TD Credit Card payments.
                • Make Canadian bill payments.
                • Deposit a cheque by taking a picture with TD Mobile Deposit.
                • Send, request and receive money within Canada using Interac e-Transfer® (1).
                • Send money internationally in more ways to more places with TD Global Transfer.
                • Get answers to many of your everyday TD banking questions 24/7, 365 days a year with TD Clari.
                • Keep track of your spending and receive real time notifications with TD MySpend (2).
                INVESTMENT ADVANTAGES:
                The TD app allows you to monitor the market, research investment ideas, and trade everything from stocks to options.
                • Act quickly on market opportunities: trade stocks, ETFs, options and multi-leg options, as well as mutual funds.
                • Help protect your portfolio from market loss with stop orders.
                • TD Direct Investing clients can now view their account performance at a glance, monitor the status of their trades and stay up to date on events relevant to their portfolio.
                • Keep tabs on your favourite securities with watchlists, which sync with WebBroker.
                • Set mobile push notifications to receive real-time price alerts for stocks, ETFs and mutual funds.
                • Interactive charts and real-time quotes can help you make informed decisions on the go.
                By clicking "Get", you consent to the installation of the TD app (3) and any future updates that can perform the functions described. The TD app is for use by customers with TD Canada Trust banking accounts and an active EasyWeb account. You may withdraw your consent at any time by deleting this app.
                IMPORTANT DISCLOSURES ABOUT THE TD APP:
                We use your mobile marketing identifier and other technologies to deliver personalized content on our websites and relevant advertising on other websites, unless you change your preferences. To update/manage these preferences on the TD app, use your device's opt-out settings. Open: Settings > Privacy > Advertising” and turn on “Limit Ad Tracking” to opt-out of interest-based ads. To manage these preferences on our websites, use your browser and select Ad Choices & Personalization at the bottom of the www.td.com homepage.
                If you require assistance, call 1-866-222-3456, mail TD CASL Office, Toronto Dominion Centre, PO Box 1, Toronto ON, M5K 1A2, or email us at customer.support@td.com.
                (1) Interac e-Transfer® is a registered trade-mark of Interac Inc. Used under license.
                (2) TD MySpend works best with the TD app. However, you do not need to download the TD app to use TD MySpend.
                (3) Provided by The TD Bank Group which includes The Toronto-Dominion Bank and its affiliates, who provide deposit, investment, loan, securities, trust, insurance and other products or services.""",
            'url_link': "https://apps.apple.com/ca/app/td-canada/id358790776"
        },
        'Scotia':{
            'date_collection': datetime.now().strftime("%Y-%m-%d"), #datetime 
            'appname': "Scotiabank",
            'category': "Finance",
            'headline': "Designed for real life", 
            'theme_color': "red",
            'name_in_icon': 0, #binary, 1: includes name, 0: does not 
            'chart_rank': 7,  #rank on chart on date this was collected
            'avg_rating': 4.7, 
            'num_ratings': 761500,
            'age_min': 4, #minimum age for use
            'price': "free",
            'num_pictures_iphone': 8, #number of screenshots of the app UI uploaded by developer for iPhone 
            'num_pictures_ipad': 5, #number of screenshots of the app UI uploaded by developer for iPad 
            'num_pictures_watch': 3, #number of screenshots of the app UI uploaded by developer for Apple Watch 
            'developer': 'Scotiabank',
            'language': ['EN','FR'], 
            'size': 193.3, #megabytes
            'device_compatible': ['iphone', 'ipad', 'apple watch'], 
            'most_frequent_stars': "5",
            'second_most_frequent_stars': "4",
            'third_most_frequent_stars': "3",
            'update_info': '2024-10-18', #Oct 18, 2024 Version 2409.0.3
            'version': '2409.0.3', 
            'latest_version_rate': 4.75,
            'latest_version_numRating': 12707,
            'data_gathered': ['financial info', 'user content', 'contact info', 'search history', 'usage data', 'identifiers', 'location', 'diagnostics'],
            'apple_watch': 1,    #supports apple watch 
            'apple_wallet': 1, #supports apple wallet
            'youmightlike': ['Borrowel: Credit Report', 'Neo Financial', 'Western Union Send Money', 'TD Insurance', 'Simplii financial', 'PC Financial Mobile'],
            'summary':"""Complete your everyday transactions with more ease, accessibility, and security — for banking that’s as flexible as it is fast.
                    Key features include:
                    Budgeting, insights, and advice:
                    Create a budget and reach your financial goals faster with personalized insights and advice from Scotia Smart Money by Advice+.
                    Rewards your way:
                    View your Scene+ points balance and redeem your rewards right in the app.
                    Mobile cheque deposit:
                    Take a photo of a cheque and deposit money quickly and easily into your account.
                    TransUnion credit score and report:
                    Check your credit score with TransUnion as often as you want, at no additional cost and zero impact to your score.
                    Barrier-free banking:
                    With features such as dynamic font sizing and VoiceOver compatibility, the app was designed with accessibility top of mind.
                    Advisor access:
                    Book an appointment to meet with a Scotiabank advisor on the phone or in-person.
                    Next-level security:
                    Data encryption keeps financial information safer, 2-step verification confirms your identity, and notifications help you stay on top of what’s happening in your accounts.
                    Switch between Scotiabank apps:
                    Sign in once and navigate easily between the Scotia mobile banking app and the Scotia iTRADE app.
                    Personalized support:
                    Find quick answers with the Scotiabank chatbot, and connect with a live chat advisor.
                    Important disclosures:
                    By pressing the button above or by downloading the mobile app published by Scotiabank, you consent to the installation of this app and to future updates and upgrades. You can withdraw your consent at any time by deleting this app, or get instructions on how to remove or disable the Scotiabank mobile app by contacting us at the address below.
                    The Scotiabank mobile app lets you manage, move, and monitor your money using your mobile phone.
                    When you use Scotiabank’s mobile deposit feature, we will access your device camera to take a picture of your cheque; record the cheque number, account number, institution transit number, and amount; record your device model, as well as its iOS version and manufacturer.
                    When you download or update this app, or when you apply for, enrol in, or use a service through mobile banking, we may collect information about your computer or device, operating system, internet connection or telephone account, settings, IP address and device locational data, and transaction data, as well as personal information.
                    We may collect, use, disclose, and retain this information as set out in the Scotiabank Privacy Agreement (scotiabank.com/ca/en/about/contact-us/privacy/privacy-agreement.html) and to determine which settings are appropriate for your computer system, to provide or enhance digital functionality and banking options, and for security purposes, internal analysis, and reporting.
                    Please note that this app gives you access to Scotiabank accounts held in Canada. For information about our services in other countries, visit scotiabank.com.
                    Have questions about the app?
                    Visit scotiabank.com/app or give us a call at 1-877-277-9303 (Canada/USA) so we can help.
                    The Bank of Nova Scotia
                    44 King St. West
                    Toronto, ON M5H 1H1""",
            'url_link': "https://apps.apple.com/ca/app/scotiabank/id341151570"
        },
        'BMO':{
            'date_collection': datetime.now().strftime("%Y-%m-%d"), #datetime 
            'appname': "BMO Mobile Banking",
            'category': "Finance",
            'headline': " ", 
            'theme_color': "blue",
            'name_in_icon': 0, #binary, 1: includes name, 0: does not 
            'chart_rank': 10,  #rank on chart on date this was collected
            'avg_rating': 4.6, 
            'num_ratings': 111300,
            'age_min': 4, #minimum age for use
            'price': "free",
            'num_pictures_iphone': 4, #number of screenshots of the app UI uploaded by developer for iPhone 
            'num_pictures_ipad': 3, #number of screenshots of the app UI uploaded by developer for iPad 
            'num_pictures_watch': 0, #number of screenshots of the app UI uploaded by developer for Apple Watch 
            'developer': 'BMO Financial Group',
            'language': ['EN','FR'], 
            'size': 124.6, #megabytes
            'device_compatible': ['iphone', 'ipad'], 
            'most_frequent_stars': "5",
            'second_most_frequent_stars': "4",
            'third_most_frequent_stars': "1",
            'update_info': '2024-09-19', #Sep 19, 2024 Version 
            'version': '6.12.0', 
            'latest_version_rate': 4.6,
            'latest_version_numRating': 133,
            'data_gathered': ['usage data', 'location', 'diagnostics', 'identifiers'], #what data the app collects
            'apple_watch': 0,    #supports apple watch 
            'apple_wallet': 1, #supports apple wallet
            'youmightlike': ['KOHO: Award-winning Money App', 'Capital One Canada', 'Tangerine Mobile Banking', 'Borrowel: Credit Report', 'Simplii Financial', 'Western Union Send Money'],
            'summary':"""With the BMO® Mobile Banking app, completing everyday transactions is quick and easy so you can get on with your day, your way. Plus, BMO Mobile Banking is safe and secure, so you can confidently bank on the go.
                    We work hard to protect your confidential information and privacy. Rest assured that you are protected by our 100 Electronic Banking Guarantee. We will reimburse you 100% for any losses to your personal bank accounts resulting from unauthorized transactions through BMO Mobile Banking. For more information please visit: bmo.com/security
                    FEATURES:
                    • View your banking, credit card and rewards, mortgage, and investment balances directly from your Account Summary. View transaction history on any of your accounts
                    • Transfer funds including cross currency and send an INTERAC e-Transfer®*
                    • Add/edit INTERAC e-Transfer recipients
                    • Pay bills, manage Payees, set up future-dated bill payments and view payment history
                    • View detailed account info, including credit card balances, due dates, minimum payments, mortgage details and funds on hold for bank accounts
                    • Book an appointment
                    • Save your most used BMO Debit Cards or BMO personal credit cards with nicknames to sign in quickly and securely
                    • Find BMO branches and ATMs
                    • Sign in using Touch ID for quick access to BMO Mobile Banking
                    • Enjoy the use of Apple Pay with your BMO Debit and Credit Cards at the cash register
                    GET STARTED:
                    To use BMO Mobile Banking, you must be registered for BMO Online Banking. Simply sign in to BMO Mobile Banking exactly as you would sign in to BMO Online Banking. If you are not registered for BMO Online Banking, visit bmo.com/onlinebanking to register today.
                    Learn more at:
                    bmo.com/mobile
                    BMO Bank of Montreal:
                    bmo.com
                    PRIVACY DISCLOSURES:
                    You acknowledge and understand that this app incl. updates or upgrades may (i) cause your device to automatically communicate with BMO’s servers to deliver the functionality described above and to record usage metrics, (ii) affect app-related preferences or data stored on your device, and (iii) collect, use and disclose personal information as set out in our BMO Digital privacy policy. You can withdraw your consent at any time by uninstalling the app. For help please contact us at:
                    BMO Bank of Montreal - Privacy.Matters@bmo.com
                    ®Registered trade-mark of Bank of Montreal
                    ®* INTERAC e-Transfer are registered trade-marks of Interac Inc. Used under license.""",
            'url_link': "https://apps.apple.com/ca/app/bmo-mobile-banking/id429080319"
        },
        'RBC':{
            'date_collection': datetime.now().strftime("%Y-%m-%d"), #datetime 
            'appname': "RBC Mobile",
            'category': "Finance",
            'headline': "Better banking", 
            'theme_color': "blue",
            'name_in_icon': 0, #binary, 1: includes name, 0: does not 
            'chart_rank': 3,  #rank on chart on date this was collected
            'avg_rating': 4.8, 
            'num_ratings': 208900,
            'age_min': 4, #minimum age for use
            'price': "free",
            'num_pictures_iphone': 10, #number of screenshots of the app UI uploaded by developer for iPhone 
            'num_pictures_ipad': 10, #number of screenshots of the app UI uploaded by developer for iPad 
            'num_pictures_watch': 4, #number of screenshots of the app UI uploaded by developer for Apple Watch 
            'developer': 'Royal Bank of Canada',
            'language': ['EN','FR'], 
            'size': 583.7, #megabytes
            'device_compatible': ['iphone', 'ipad', 'apple watch'], 
            'most_frequent_stars': "5",
            'second_most_frequent_stars': "4",
            'third_most_frequent_stars': "3",
            'update_info': '2024-10-08', #Oct 8, 2024 Version 6.46
            'version': '6.46', 
            'latest_version_rate': 4.7,
            'latest_version_numRating': 2090,
            'data_gathered': ['financial info', 'contact info', 'user content', 'search history', 'contacts', 'usage data', 'location', 'diagnostics', 'identifiers'], #what data the app collects
            'apple_watch': 1,    #supports apple watch 
            'apple_wallet': 1, #supports apple wallet
            'youmightlike': ['Western Union Send Money', 'Borrowel: Credit Report','Neo Financial', 'KOHO: Award-winning Money App', 'TD Insurance', 'Amex Canada'],
            'summary': """The RBC Mobile* app takes mobile banking to the next level. Everyday banking is always convenient, but our app helps make managing your money even easier. Our fresh and intuitive design gives you easy access to everything you'd expect from a banking app: account balances, money transfers, bill payments, cheque deposits, ATM locations and more. But we didn't stop there. We made it easier to find each feature with improved navigation. Our Action Button and Manage Menu take the most important tools and put them right at your fingertips. The best part? These menus are tailored to each page.
                    Exclusive to the RBC Mobile app, NOMI plays a big part of the app experience. NOMI Insights help you manage your day-to-day finances with personalized tips and spend trends. NOMI Find & Save helps make saving easy by taking a look at your spending habits to find a little extra money and saves it for you – so you don't have to.
                    We know you'll love everything the RBC Mobile app offers, and we want you to feel safe and secure using it. Starting at sign in, we've given you access to the latest in biometric identification technology, like Touch ID or Face ID, so you can securely access the app without having to remember your password. If you misplace your credit card, use the app to temporarily lock your card.
                    PRIVACY RBC collects, uses and discloses the information that you provide to us in accordance with your account agreement(s) with us and our privacy policy, available at http://www.rbc.com/privacysecurity/ca/our-privacy-principles.html
                    Learn more about RBC digital channel privacy at http://www.rbc.com/privacysecurity/ca/online-privacy.html.
                    The RBC Mobile app might need to access device services for certain features, like finding nearby RBC Royal Bank® branches. For a full list of the features, check out http://www.rbcroyalbank.com/mobile/permissions/mobile-iOS.html.
                    For help removing the RBC Mobile app from your device, there are instructions at http://www.rbcroyalbank.com/mobile/permissions/mobile-iOS.html or you can contact mobile.feedback@rbc.com.
                    LEGAL:
                    RBC does not sell, promote or otherwise provide financial services or products referred to in this app outside of Canada. You should not access this app if you are not a resident of Canada.
                    When you select to install the RBC Mobile app, you're consenting to any future updates or upgrades. Depending on your device, operating system or user-initiated settings, these might be automatically installed. You're able to withdraw your consent by uninstalling the RBC Mobile app from your device.
                    If you download the RBC Mobile app, you must review, and are subject to, the terms & conditions found under the Legal link on www.rbc.com as well as all applicable agreements between you and any RBC company, including:
                    - Electronic Access Agreement (Personal clients of Royal Bank of Canada)
                    - Business Account Agreement (Business clients of Royal Bank of Canada)
                    - The Operation of Account Agreement (RBC Direct Investing clients)
                    - General Account Agreement (RBC Dominion Securities clients)
                    *The RBC Mobile app is operated by:
                    Royal Bank of Canada
                    10 York Mills Rd. 3rd Floor
                    Toronto, ON M2P 0A2
                    www.rbcroyalbank.com
                    1-800-769-2511
                    mobile.feedback@rbc.com
                    RBC Direct Investing Inc.
                    Royal Bank Plaza
                    200 Bay Street, North Tower, P.O. Box 75
                    Toronto, ON, M5J 2Z5
                    www.rbcdirectinvesting.com
                    RBC Dominion Securities Inc.
                    155 Wellington Street West, 17th Floor
                    Toronto, ON, M5V 3K7
                    www.rbcwealthmanagement.com
                    ®/™ Trademarks of Royal Bank of Canada. RBC and Royal Bank are registered trademarks of Royal Bank of Canada.
                    Touch ID, Face ID, Siri and iMessage are trademarks of Apple Inc., registered in the U.S. and other countries.""",
            'url_link': "https://apps.apple.com/ca/app/rbc-mobile/id407597290"
        }
    }
]