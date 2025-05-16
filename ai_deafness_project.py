# AI & Deafness Educational Script
# Author: Sandra White-Belgrave
# Run in: VS Code
# Purpose: To teach about AI bias, Deafness, and ethical fairness

def welcome():
    print("=" * 50)
    print("🎓 Welcome to AI & Deafness Learning Tool")
    print("=" * 50)
    print("This project explores how AI affects Deaf and disabled people.")
    print("You'll learn about real-life stories and why ethics matter.\n")

def show_menu():
    print("\nChoose a case to learn more:")
    print("1. COMPAS & Racial Bias")
    print("2. Deaf Man Jailed Without Interpreter")
    print("3. Amazon AI Hiring Bias")
    print("4. Facial Recognition Bias")
    print("5. Exit")
    print("6. Try AI Risk Calculator")  # NEW OPTION

def show_case(choice):
    if choice == "1":
        print("\n🔍 COMPAS & Racial Bias:")
        print("In 2016, ProPublica found COMPAS was twice as likely to label Black people as 'high risk' unfairly.")
        print("Imagine this bias applied to a Deaf person with no communication support.")
        print("📎 Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing\n")
    elif choice == "2":
        print("\n🔍 Deaf Man Jailed Without Interpreter:")
        print("William Pierce, a Deaf man, spent 25 days in jail with no interpreter.")
        print("He missed hearings, medical help, and his rights were ignored.")
        print("📎 Source: https://www.nbcwashington.com/news/local/deaf-man-jailed-without-sign-language-translator-wins-case-against-dc-jail/1976499/\n")
    elif choice == "3":
        print("\n🔍 Amazon AI Hiring Bias:")
        print("Amazon had to shut down an AI hiring tool that unfairly favored men over women.")
        print("This shows how AI can exclude disabled people if trained on biased data.")
        print("📎 Source: https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G\n")
    elif choice == "4":
        print("\n🔍 Facial Recognition Bias:")
        print("Studies found facial recognition often fails on darker skin and disabled faces.")
        print("This is dangerous when AI is used in policing or access control.")
        print("📎 Source: https://www.aclu-mn.org/en/news/biased-technology-automated-discrimination-facial-recognition\n")
    elif choice == "5":
        print("\nThank you for exploring how AI affects fairness in the real world!")
        print("Remember: AI is powerful, but it must be fair to everyone — especially those often left out.\n")
    elif choice == "6":
        risk_calculator()
    else:
        print("\n⚠️ Invalid choice. Please enter a number from 1 to 6.\n")

def risk_calculator():
    print("\n📊 AI Risk Calculator (Mock Example)")
    print("Answer the following questions with 'yes' or 'no':\n")

    support = input("Did the person receive proper Deaf/disability support? ").lower()
    record = input("Does the person have a previous criminal record? ").lower()
    communication = input("Did the person face communication barriers during interview or court? ").lower()

    risk_score = 0

    if record == "yes":
        risk_score += 2
    if communication == "yes":
        risk_score += 2
    if support == "no":
        risk_score += 2

    print("\n🧾 Result:")

    if risk_score >= 5:
        print("⚠️ High Risk — This is what AI might predict without full understanding.")
    elif risk_score >= 3:
        print("⚠️ Medium Risk — AI may assume uncertainty or slight danger.")
    else:
        print("✅ Low Risk — AI sees this person as unlikely to reoffend.")

    print("\n💡 Note: This result is just a simulation. AI systems like COMPAS may be biased if they don’t account for disability or Deaf access. Fairness matters!\n")

# Main Program
welcome()
show_menu()

while True:
    user_input = input("\nEnter your choice (1-6): ")
    show_case(user_input)
    if user_input == "5":
        break
    show_menu()
# End of the script