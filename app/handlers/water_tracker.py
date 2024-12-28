# Calculates daily water intake: weight * 30ml for women, 40ml for men, 35ml if gender is unknown
def get_daily_water_goal(weight, gender):
    if gender == "m":#male
        return weight * 40
    if gender == "f":#female
        return weight * 0,3
    if gender == "u":#unknow
        return weight * 0,35

