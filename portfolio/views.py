from django.shortcuts import render
from portfolio.models import Introduce, Experience, Skill

import datetime


def getPortfolioIntroduce(request):
    template = 'portfolio/index.html'
    context = { 
        "introduce": getIntroduce(),
        "education" : getExperience("E"),
        "projects" : getExperience("P"),
        "skills" : getSkills(),
        "services" : getExperience("S"),
    }

    return render(request, template, context)


def getIntroduce():
    introduce = Introduce.objects.all().order_by("id").reverse()[0]
    responseData = {
        "name": introduce.name, 
        "job": introduce.job, 
        "aboutMe": introduce.aboutMe, 
        "address": introduce.address, 
        "age": introduce.age
    }

    return responseData


def getExperience(experienceDivsCd):
    experienceList = Experience.objects.all().filter(experinceDivsCd=experienceDivsCd).order_by("strtDate").reverse()

    responseList = []
    for experience in experienceList:
        responseList.append({
            "date" : datetime.datetime.strftime(experience.strtDate, '%y.%m') + " ~ " + datetime.datetime.strftime(experience.endDate, '%y.%m'),
            "title" : experience.title,
            "subTitle" : experience.subTitle,
            "content" : experience.content
        })

    return responseList


def getSkills():
    skillList = Skill.objects.all()

    responseList = []
    for experience in skillList:
        responseList.append({
            "name" : experience.name,
            "proficiency" : experience.proficiency
        })

    return responseList