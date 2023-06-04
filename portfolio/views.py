from django.shortcuts import render

def getPortfolioIntroduce(request):
    template = 'portfolio/index.html'
    context = { 
        "introduce": getIntroduce(),
        "study" : getStudy(),
        "exprience" : getExperience(),
        "skills" : getSkills(),
        "services" : getService(),
    }

    return render(request, template, context)

def getIntroduce():
    introduce = {
        "name": "강형구",
        "job": "Software Engineer",
        "aboutMe" : "",
        "address" : "Seoul, South Korea",
        "age" : "31",
    }

    return introduce

def getStudy():
    study = [
        {
            "date" : "23.09",
            "title" : "SQLD",
            "subTitle" : "Lisence",
            "content" : "Kdata 데이터자격검정, SQL Developer"
        },
        {
            "date" : "14.03 ~ 21.02",
            "title" : "경희대학교 졸업",
            "subTitle" : "University",
            "content" : "소프트웨어융합대학 컴퓨터공학과 학사 졸업"
        },
    ]

    return study

def getExperience():
    experience = [
        {
            "date" : "21.11 ~ Current",
            "title" : "차세대 UCube 프로젝트",
            "subTitle" : "LG CNS",
            "content" : "LG U+의 차세대 UCube 상담파트 설계 및 개발 참여 \nFE(WebSqaure), BE(Spring Boot, MariaDB), MSA, Rest API, Kafka, MySQL"
        },
    ]

    return experience

def getSkills():
    skills = [
        {
            "name" : "java",
            "proficiency" : "80%"
        }
    ]

    return skills

def getService():
    services = [
        {
            "date" : "21.11 ~ Current",
            "title" : "title",
            "subTitle" : "subTitle",
            "content" : "Something"
        }
    ]

    return services