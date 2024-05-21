import csv
import datetime as dt
import pendulum as pn


def collect_birthdays_this_month():
    final_bd_list = []
    current_date = dt.datetime.now().date()
    with open('/Users/ezrakrupka/PycharmProjects/Family_Birthdays_Project/core_files/birthdays.csv') as file:
        contents = csv.DictReader(file, fieldnames=['Name', 'Birthday'])
        next(contents)
        clean_data = list(contents)

    for i in clean_data:
        birthday = i['Birthday']
        name = i['Name']
        parse_bd = dt.datetime.strptime(birthday, '%Y-%m-%d').date()
        if current_date.month == parse_bd.month:
            final_bd_list.append({name: parse_bd})

    messages = birthday_alert(final_bd_list)
    return messages


def birthday_alert(data):
    messages = []
    current_time = dt.datetime.now()
    current_set_time = current_time.replace(hour=00, minute=00, second=00)

    for entry in data:
        for name,birthday in entry.items():
            current_date = pn.instance(current_set_time)
            pn_birthday = pn.instance(birthday)
            if current_date.month == pn_birthday.month:
                diff = pn_birthday.day - current_date.day
                if diff == 7:
                    messages.append(f'\n{name.title()}\'s Birthday Is Exactly 1 Week Away!')
                if diff == 1:
                    messages.append(f'\n{name.title()}\'s Birthday Is Tomorrow!')
                if diff == 0:
                    messages.append(f'\nToday is {name.title()}\'s  Birthday!')
    return messages


if __name__ == '__main__':
    print(collect_birthdays_this_month())

