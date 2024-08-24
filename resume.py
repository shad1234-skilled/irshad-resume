#!/usr/bin/env python
# coding: utf-8

# In[6]:


import base64
import streamlit as st
from PIL import Image
import time


def show_component_with_delay(component_function, delay=0.5):
    time.sleep(delay)
    component_function()
    
def type_text(placeholder, text, delay=0.03):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"<p style='text-align: left; font-size: 18px;'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)
    
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#####################
# Header 
#  text content

def gradient(color1, color2, color3, content1, content2):
    
    container = st.empty()
    
    with container.container():
        st.markdown(f'''
        <div style="
            background: linear-gradient(to right, {color1}, {color2});
            padding: 20px;
            border-radius: 10px;
            text-align: left;
            font-size: 24px;
            color: {color3};
            max-width: 800px;
            margin: auto;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
            <h1 style="font-size: 50px;">{content1} 👋</h1>
            <div id="typing-effect"></div>
        </div>
        ''', unsafe_allow_html=True)
    
    #placeholder1 = st.empty()
    
    type_text(container, content2)

markdown_text = """
Welcome to my professional digital profile. Here, you’ll find a comprehensive
summary of my professional journey, accomplishments, and the skills I have 
developed over the years. This will help you understand my experiences and expertise.
"""

with st.container():
    gradient('#B5B5B5','#008080','e0fbfc',f"Greetings, I am Irshad", markdown_text)

#st.title("Greetings, I am Irshad 👋" )
#type_text("Greetings, I am Irshad 👋")

st.markdown("<br>", unsafe_allow_html=True)
#type_text(markdown_text)

# Display markdown with typing effect
#st.markdown("")
#type_text(markdown_text)


image = Image.open(r"C:\Users\lenovo\Pictures\Camera Roll\image.JPG")

# def set_background_color(color):
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-color: {color};
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
 
def sidebar():
    st.markdown("""
        <style>
            /* Fix sidebar and show collapse button */
            .css-1d391kg {
                /* Remove display: none; to show the collapse button */
            }
            .css-1y4p8pa {
                width: 300px !important;  /* Control sidebar width */
                position: fixed;
                top: 0;
                left: 0;
                height: 200vh;
                padding-top: 1rem;
            }
            /* Adjust content to start after sidebar */
            .css-18e3th9 {
                margin-left: 300px !important;
            }
            /* Navbar adjustments */
            nav {
                margin-left: 300px;
            }
            /* Sidebar image container */
            .sidebar-image {
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    
        <script>
            // Adjust the navbar position when the sidebar is collapsed or expanded
            const sidebar = document.querySelector('.css-1y4p8pa');
            const content = document.querySelector('.css-18e3th9');
            const navBar = document.querySelector('nav');
    
            sidebar.addEventListener('transitionend', function() {
                if (window.getComputedStyle(sidebar).width === '0px') {
                    content.style.marginLeft = '0px';
                    navBar.style.marginLeft = '0px';
                } else {
                    content.style.marginLeft = '300px';
                    navBar.style.marginLeft = '300px';
                }
            });
        </script>
    """, unsafe_allow_html=True)
    
    # Sidebar - Profile Picture and Contact Information
    #st.sidebar.markdown('<div class="sidebar-image"><img src="C:\\Users\\lenovo\\Pictures\\Camera Roll\\image.JPG"></div>', unsafe_allow_html=True)
    st.sidebar.image(image)
    st.sidebar.markdown("# Mohammad Irshad Khan, B.Sc. (Maths)")
    st.sidebar.markdown("### Data Scientist | Data Science Manager")
    st.sidebar.write("📱 Mobile: +91 - 8830 173428")
    st.sidebar.write("📍 Location: Pune, India")
    st.sidebar.write("📧 Email: mohammadirshad.khan@rediffmail.com")
    st.sidebar.write("🌐 [LinkedIn](https://www.linkedin.com/in/mohammad-irshad-khan-06242b255/) | [GitHub](https://github.com/yourprofile)")

    
def navigation_bar():
    #####################
    # Navigation
    
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #008080;">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="C:\\Users\\lenovo\\Desktop\\TCS\\MLOps Udemy\\Streamlit\\my app\\resume.pdf" download>Download Resume <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#certifications" style="color: #FFFFFF;">Certifications</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#skills" style="color: #FFFFFF;">Skills Proficiencies</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#work-experience" style="color: #FFFFFF;">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#project-summary" style="color: #FFFFFF;">Projects Summary</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#education" style="color: #FFFFFF;">Education</a>
          </li>
          </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)

def main_content():
    st.markdown('## Career Summary', unsafe_allow_html=True)
    st.info('''
    •	Results-driven Data Science Manager with 5 years of experience of building and empowering high-performing cross-functional data science teams.
    
    •	Proficient in data science project management methodologies CRISP, DDS, Agile and Scrum, to drive effective knowledge discovery and collaborative project management.
    
    •	Adept at extract actionable insights from complex data and translating business needs into actionable insights through the entire data science lifecycle.
    
    •	Proven ability to build and lead teams in creating robust Machine Learning and Deep Learning models, including CNN, RNN, LSTM solutions to meet business objectives. 
    
    •	Strong leadership and management skills in various data analysis and modeling techniques, including feature selection, regression, clustering, classification, and neural networks.
    
    •	I have expertise in Python, SQL, advanced statistical methodologies and machine learning techniques to deliver impactful solutions while bridging the gap between technical and business stakeholders through continuous communication and collaboration skills.
    
    •	I am passionate about staying abreast of emerging technologies and industry trends to continuously enhance team capabilities, fostering promising talent through training and mentorship to elevate team expertise and performance to deliver impactful business solutions.
    
    •	Hands-on experience of Descriptive, Diagnostic, Predictive, Prescriptive, Exploratory Data Analysis, Inferential Statistical analysis, Hypothesis and A/B testing
    
    ''')
    
    
    
    #####################
    # Custom function for printing text
    def txt(a):
      st.markdown(a)
    
    def txt1(a, b):
      col1, col2 = st.columns([4,1])
      with col1:
        st.markdown(a)
      with col2:
        st.markdown(b)
    
    def txt2(a, b):
      col1, col2 = st.columns([1,4])
      with col1:
        st.markdown(f'`{a}`')
      with col2:
        st.markdown(b)
    
    def txt3(a, b):
      col1, col2 = st.columns([1,2])
      with col1:
        st.markdown(a)
      with col2:
        st.markdown(b)
      
    def txt4(a, b, c):
      col1, col2, col3 = st.columns([1.5,2,2])
      with col1:
        st.markdown(f'`{a}`')
      with col2:
        st.markdown(b)
      with col3:
        st.markdown(c)
    
    ###############
    
    st.markdown('''
    ## Certifications
    ''')
    
    #txt('** Certifications **')
    
    st.markdown('''
    •  GCP Professional Machine Learning Engineer
    
    •  GCP Cloud Digital Leader
    
    •	Microsoft Azure Data Scientist Associate
    
    •	Organization Certified Agile Champion
    
    •	Lean Six Sigma Green Belt
    ''')
    
    
    #####################
    st.markdown('''
    ## Skills Proficiencies
    ''')
    txt3('Machine Learning Techniques', '`Regression`, `Classification`, `Clustering`, `NLP`, `Reinforcement Learning`')
    txt3('Deep Learning Techniques', '`CNN`, `RNN`, `LSTM`, `Computer Vision`, `Transformers`')
    txt3('Machine Learning Libraries', '`scikit-learn`, `TensorFlow`, `Keras`')
    txt3('Data visualization', '`matplotlib`, `seaborn`')
    txt3('Languages and Tools', '`Python`, `SQL`, `Numpy`, `Pandas`, `Tableau`, `Power-BI`')
    txt3('Cloud Experience', '`GCP`, `Azure`, `AWS`')
    txt3('Big Data Architecture', '`Hadoop`, `HDFS`, `Hive`, `Spark`, `MapReduce`')
    txt3('Project Management', '`Agile-Scrum Management`, `Business Analytics`, `Cloud Resource Management`, `Stakeholders Management`')
    
    
    #####################
    st.markdown('''
    ## Work Experience
    ''')
    
    txt1('**Data Science Manager TATA Consultancy Services (TCS)**', '01/2019 – Present')
    st.markdown('''
    •	Understand and document the analytic needs of business users.
    
    •	Work with huge volumes of data to solve real-world problems that feed into our platform to be used by downstream applications.
    
    •	Mine and analyze data from corporate databases to optimize and improve product development, marketing techniques and business strategies.
    
    •	Assess the effectiveness and accuracy of new data sources and data gathering techniques and develop custom data models to apply to the data sets.
    
    •	Develop and define project scope, objectives, and deliverables in collaboration with stakeholders.
    
    •	Establish a detailed project plan, including timelines, milestones, and resource allocation.
    
    •	Assemble cross-functional teams comprising data scientists, analysts, engineers, and other key stakeholders.
    
    •	Facilitate regular meetings to review project progress, obstacles, and next steps.
    
    •	Act as the main point of contact between stakeholders, including senior management, clients, and the data science team.
    
    •	Prepare and deliver regular project updates through presentations, reports, and dashboards.
    •	Oversee the creation of project documentation, including project plans, code documentation, and user manuals.
    •	Ensure proper archiving of data, codes, and models for future reference.
    •	Experience working with Big Data Technologies: Apache Hadoop, Apache hive & Apache Spark
    •	Translate business questions into clear and solvable data science problems and Maximize value of existing data assets
    •	Working with business on translating broad problem statements to solvable data science problems
    •	Understand Data Science Algorithms & Coding complexities pre-processing and feature engineering to problem modeling and Hyper parameter tuning.
    
    ''')
    
    txt1('**Operations Delivery Manager TATA Consultancy Services (TCS)**', '03/2013 – 12/2018')
    st.markdown('''
    •	3+ years of experience of managing team of 200+ associates across 3 locations, ensuring management and employees’ full understanding of business needs, auditing compliance, tracking progress towards goals
    •	Business Development, Knowledge management, process management, planning and managing offshore performance, client management, process simplification and automation
    •	Expertise in Working on Billings, External and Internal Audits, regular client reviews and client Surveys.
    •	Rich Expertise in Managing team, Process Training, interacting with clients from various cultures, consistently achieving SLA targets and maintaining higher customer satisfaction score.
    •	Promoting an environment where product knowledge is appreciated and equal opportunity is given to learn and grow, which also helps in creating backup for all Trainer, Quality Checker, SME and Leadership roles.
    •	Hands on experience with regards to Risk Management, deploying controls for mitigation, Control and Self -Assessment
    
    ''')
    
    
    txt1('**Senior Associate Automatic Data Processing (ADP)**', '07/2010 – 07/2012')
    st.markdown('''
    •	Worked in the Pilot Batch and was part of the team who set-up the process in Pune. 
    •	Trained the new joiners associates in Implementation.
    •	Was the first associate to get trained in 4 different work types.
    
    ''')
    
    txt1('**Senior Associate WNS Global Services (WNS)**', '10/2007 – 06/2010')
    st.markdown('''
    •	Was the fastest to complete L3 accreditation for ledger management process.
    •	Was the winner in the process contest.
    
    ''')
    
    
    #####################
    st.markdown('''
    ## Projects Summary 
    ''')
    txt2('Loan Risk Optimization', 'Executed a project to optimize loan approval processes using predictive analytics. Developed a predictive model to assess loan risk and automate decision-making using Gen AI, reducing approval time by 30% and improving overall loan portfolio performance.')
    txt2('Supply Chain Analytics', 'Implemented a supply chain analytics solution utilizing LLM for optimizing inventory management in a retail supply chain. Utilized machine learning algorithms to forecast demand, taking into account seasonality and market trends. The system dynamically adjusted reorder points, reducing excess inventory by 15% and minimizing stockouts. The predictive analytics-driven approach improved overall supply chain efficiency and customer satisfaction.')
    txt2('Retail Demand Forecasting', 'Implemented demand forecasting algorithms for a retail supply chain, leveraging historical data and external factors. Improved inventory management, reducing stockouts by 15% and excess inventory by 10%.')
    txt2('E-Commerce NLP Analysis', 'Conducted customer communication analysis for an e-commerce platform. Leveraged natural language processing (NLP) to analyze customer emails and support tickets. Identified common issues and sentiment trends, leading to targeted improvements in product information and customer support processes.')
    txt2('Banking Chatbot Integration', 'Implemented a chatbot for a banking institution. Enabled customers to perform routine banking tasks, check account balances, and receive personalized financial advice. Integrated with backend systems for secure transactions. The chatbot improved customer engagement, providing quick and convenient support for common queries.')
    txt2('Customer Support Automation', 'Implemented customer communication analysis for an online retail platform. Integrated with customer support systems to provide instant assistance with order tracking, returns, and product inquiries. Implemented natural language understanding (NLU) to enhance user interactions, resulting in a 20% reduction in customer service response time.')
    
    
    #####################
    st.markdown('''
    ## Education
    ''')
    
    txt('**Bachelors of Science** (Maths)')
    txt('*Jabalpur University, Madhya Pradesh*')
    txt('July 2002 - June 2005')


#####################
#st.markdown('''
## Social Media
#''')
#txt2('LinkedIn', 'https://www.linkedin.com/in/mohammad-irshad-khan-06242b255/')
#txt2('GitHub', 'https://github.com/')


# In[7]:


if __name__ == '__main__':
    # Display header and introduction
    #show_component_with_delay(header_and_intro, delay=0.5)
       
    # Display sidebar
    show_component_with_delay(sidebar, delay=0.5)
    
    # Display navigation bar
    show_component_with_delay(navigation_bar, delay=0.5)
    
    # Display main content
    show_component_with_delay(main_content, delay=0.5)


# In[ ]:




