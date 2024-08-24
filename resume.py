#!/usr/bin/env python
# coding: utf-8

# In[5]:


import base64
import streamlit as st
from PIL import Image
import time
from pathlib import Path

def show_component_with_delay(component, delay=0.0):
    time.sleep(delay)
    component()
    
def type_text(placeholder, text, delay=0.04):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"<p style='text-align: left; font-size: 18px;'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)
    
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


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
    
       
    type_text(container, content2)

markdown_text = """
Welcome to my professional digital profile. Here, you’ll find a comprehensive
summary of my professional journey, accomplishments, and the skills I have 
developed over the years. This will help you understand my experiences and expertise.

Download my detailed resume in pdf format for more information on my skills and experience.
"""

with st.container():
    gradient('#B5B5B5','#008080','e0fbfc',f"Greetings, I am Irshad", markdown_text)

st.markdown("<br>", unsafe_allow_html=True)
#type_text(markdown_text)

image = Image.open('image.png')

pdf_url = "https://raw.githubusercontent.com/shad1234-skilled/irshad-resume/main/my_resume.pdf"

 
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
                style="background-color: #e2FFFF;
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

    st.sidebar.image(image)
    st.sidebar.markdown("# Mohammad Irshad Khan, B.Sc. (Maths)")
    st.sidebar.markdown("### Data Scientist | Data Science Manager")
    st.sidebar.write("📱 Mobile: +91 - 8830 173428")
    st.sidebar.write("📍 Location: Pune, India")
    st.sidebar.write("📧 Email: mohammadirshad.khan@rediffmail.com")
    st.sidebar.write("🌐 [LinkedIn](https://www.linkedin.com/in/mohammad-irshad-khan-06242b255/) | [GitHub](https://github.com/shad1234-skilled)")
    st.sidebar.markdown(f"""
    <a href="{pdf_url}" download="my_resume.pdf">
      <button style="background-color: #FF876e; color: white; border: none; padding: 5px 20px; border-radius: 5px; cursor: pointer; width: 100%;">
        Download Resume
      </button>
    </a>
    """, unsafe_allow_html=True)
    
def navigation_bar():
    #####################
    # Navigation
    
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
        
    st.markdown(f"""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #008080;">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="true" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="{pdf_url}" download="my_resume.pdf">
            <button style="background-color: #FF876e; color: white; border: none; padding: 5px 20px; border-radius: 5px; cursor: pointer;">
            Download Resume</button><span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#certifications" style="color: #FFFFFF;">Certifications</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#skills-proficiencies" style="color: #FFFFFF;">Skills Proficiencies</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#work-experience" style="color: #FFFFFF;">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#projects-summary" style="color: #FFFFFF;">Projects Summary</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#education" style="color: #FFFFFF;">Education</a>
          </li>
          </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)

def main_content():

    st.markdown(
        """
        <style>
        .reduce-space {
            margin-bottom: -20px; /* Adjust this value to control the space */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="reduce-space"></div>', unsafe_allow_html=True)
    st.markdown('## Career Summary', unsafe_allow_html=True)
    st.info('''
    •	Results-driven Data Science Manager with 5+ years of Experienced, skilled in building high-performing teams and leading data science projects using CRISP, DDS, Agile, and Scrum methodologies.
    
    •	Proficient in Python, SQL, and advanced statistical methods, with expertise in creating Machine Learning and Deep Learning models to meet business objectives.
    
    •	Passionate about emerging technologies, fostering talent through mentorship, and translating complex data into actionable business insights.
    
    ''')
    
    #####################
    # Custom function for printing text
    def txt(a):
        st.markdown(a)
    
    def txt1(a, b):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f'<div style="background-color: #008080; color: #FFFFFF;">{a}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div style="background-color: #008080; color: #FFFFFF;">{b}</div>', unsafe_allow_html=True)
    
    def txt2(a, b):
        col1, col2 = st.columns([1,4])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(f'<span style="color: 217dbb; background-color: transparent;">{b}</span>', unsafe_allow_html=True)
    
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
    
    txt1('Data Science Manager TATA Consultancy Services (TCS)', '01/2019 – Present')
    st.markdown('''
    •	Understand and document business users’ analytic needs, translating broad problem statements into solvable data science problems using technologies like tensorflow, ML algorithms, Deep learning, NLP.
    
    •	Work with large data volumes to solve real-world problems, mining and analyzing data to optimize product development, marketing techniques, and business strategies.
    
    •	Develop project scope, objectives, and deliverables, establish detailed project plans, and assemble cross-functional teams for effective project management.

    •	Facilitate regular meetings, act as the main contact between stakeholders, and deliver project updates through presentations, reports, and dashboards.

    •	Apply data science algorithms and coding complexities, including pre-processing, feature engineering, problem modeling, and hyperparameter tuning, to maximize the value of data assets.
    ''')
    
    txt1('Operations Delivery Manager TATA Consultancy Services (TCS)', '03/2013 – 12/2018')
    st.markdown('''
    •	Over 3 years of experience managing a team of 200+ associates across multiple locations, ensuring compliance, auditing, and tracking progress towards business goals.
    
    •	Expertise in business development, process management, client management, and process simplification, with hands-on experience in billings, audits, and client reviews.
    
    •	Proven ability in team management, process training, and risk management, consistently achieving SLA targets and maintaining high customer satisfaction scores.
    
    ''')
    
    
    txt1('Senior Associate Automatic Data Processing (ADP)', '07/2010 – 07/2012')
    st.markdown('''
    •	Performed a key role in establishing the process in Pune as part of the Pilot Batch.
    
    •	Trained new associates in Implementation and was the first to be trained in four different work types.
    
    ''')
    
    txt1('Senior Associate WNS Global Services (WNS)', '10/2007 – 06/2010')
    st.markdown('''
    •	Quickly completed L3 accreditation for ledger management and won the process contest.
    
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


if __name__ == '__main__':
    navigation_bar()
    sidebar()
    main_content()
    #gradient('#B5B5B5','#008080','e0fbfc',f"Greetings, I am Irshad", markdown_text)


# In[ ]:




