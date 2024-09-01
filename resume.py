from tabulate import tabulate

def get_resume_data():
    # Collect basic information
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Collect education details
    education = []
    print("\nEnter your education details (type 'done' when finished):")
    while True:
        degree = input("Degree: ")
        if degree.lower() == 'done':
            break
        institution = input("Institution: ")
        year = input("Year of Graduation: ")
        education.append([degree, institution, year])
    
    # Collect work experience
    work_experience = []
    print("\nEnter your work experience (type 'done' when finished):")
    while True:
        job_title = input("Job Title: ")
        if job_title.lower() == 'done':
            break
        company = input("Company: ")
        years = input("Years Worked (e.g., 2018-2020): ")
        work_experience.append([job_title, company, years])

    # Collect skills
    skills = input("\nEnter your skills (separated by commas): ").split(',')

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "education": education,
        "work_experience": work_experience,
        "skills": skills,
    }

def create_resume_table(data):
    # Creating the header
    print("\nResume")
    print("=" * 40)

    # Basic Information
    print("Basic Information:")
    print(tabulate([[data['name'], data['email'], data['phone'], data['address']]], 
                   headers=["Name", "Email", "Phone", "Address"], tablefmt="grid"))
    
    # Education
    if data['education']:
        print("\nEducation:")
        print(tabulate(data['education'], headers=["Degree", "Institution", "Year"], tablefmt="grid"))
    
    # Work Experience
    if data['work_experience']:
        print("\nWork Experience:")
        print(tabulate(data['work_experience'], headers=["Job Title", "Company", "Years"], tablefmt="grid"))

    # Skills
    if data['skills']:
        print("\nSkills:")
        for skill in data['skills']:
            print(f"- {skill.strip()}")
    
if __name__ == "__main__":
    resume_data = get_resume_data()
    create_resume_table(resume_data)
