import random
def get_users(user_login_password=""):
    user = {
    "id": 123,
    "name": "Egor Rusnov",
    "password": "QwEwQ7",
    "post": "Junior",
    "tests":
    [
        {
    "name": "eee",
    "theme": "rock",
    "result": 50,
    "max_result": 100,
    "typeOfTest": "0 - без записи (учебка) | 1 - запись (зачет)",
    "date": 15153135,
    "test": [
        {
            "question": "who",
            "answer": "me",
            "key": "me",
            "balls": 1
        }, {
            "question": "кто такой gir",
            "answer": "ya",
            "key": "notme",
            "balls": 0
        }
    ]
},
        {
    "name": "eee",
    "theme": "rock",
    "result": 50,
    "max_result": 100,
    "typeOfTest": "0 - без записи (учебка) | 1 - запись (зачет)",
    "date": 15153135,
    "test": [
        {
            "question": "who",
            "answer": "me",
            "key": "me",
            "balls": 1
        }, {
            "question": "кто такой gir",
            "answer": "ya",
            "key": "notme",
            "balls": 0
        }
    ]
}
    ]
}
    users = []
    for i in range(5):
        users.append(user)
        users[i]["id"] = random.randint(1, 10000)

    return users

def get_all_tests(user={}):
    # getting all tests of user(completed and not) and returning list of tests
    testss = [{
        "name": "Тест по анатомии",
        "id": random.randint(1, 10000),
        "theme": "theme",
        "max_result": 100,
        "questions": [
            {
                "question": "Есть над чем задуматься: ключевые особенности структуры проекта являются только методом политического участия и описаны максимально подробно. Высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта: понимание сути ресурсосберегающих технологий говорит о возможностях поставленных обществом задач. Идейные соображения высшего порядка, а также сплочённость команды профессионалов играет важную роль в формировании переосмысления внешнеэкономических политик. Следует отметить, что экономическая повестка сегодняшнего дня, в своём классическом представлении, допускает внедрение кластеризации усилий. Банальные, но неопровержимые выводы, а также действия представителей оппозиции функционально разнесены на независимые элементы. Также как социально-экономическое развитие однозначно фиксирует необходимость своевременного выполнения сверхзадачи. Как принято считать, базовые сценарии поведения пользователей, вне зависимости от их уровня, должны быть функционально разнесены на независимые элементы. Внезапно, ключевые особенности структуры проекта освещают чрезвычайно интересные особенности картины в целом, однако конкретные выводы, разумеется, описаны максимально подробно. А также непосредственные участники технического прогресса представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть преданы социально-демократической анафеме. Равным образом, консультация с широким активом играет определяющее значение для первоочередных требований. В своём стремлении улучшить пользовательский опыт мы упускаем, что явные признаки победы институционализации, инициированные исключительно синтетически, заблокированы в рамках своих собственных рациональных ограничений. Безусловно, сложившаяся структура организации однозначно фиксирует необходимость экономической целесообразности принимаемых решений. Однозначно, непосредственные участники технического прогресса будут заблокированы в рамках своих собственных рациональных ограничений. Как уже неоднократно упомянуто, сделанные на базе интернет-аналитики выводы призывают нас к новым свершениям, которые, в свою очередь, должны быть объединены в целые кластеры себе подобных. Задача организации, в особенности же выбранный нами инновационный путь позволяет оценить значение экспериментов, поражающих по своей масштабности и грандиозности. Господа, глубокий уровень погружения способствует подготовке и реализации распределения внутренних резервов и ресурсов. Разнообразный и богатый опыт говорит нам, что начало повседневной работы по формированию позиции в значительной степени обусловливает важность форм воздействия. Противоположная точка зрения подразумевает, что многие известные личности являются только методом политического участия и заблокированы в рамках своих собственных рациональных ограничений. Являясь всего лишь частью общей картины, действия представителей оппозиции призывают нас к новым свершениям, которые, в свою очередь, должны быть объединены в целые кластеры себе подобных.",
                "type": 1,
                "variants_of_answer": ["1 мама я в ютубе ковыряюсь и нахожу видео где дядя берёт огромных размеров жабу и после кидает её на сковородку без зазрения совести а после жарит и ест как ни в чём не бывало, ну ты представляешь, мама?", "2 такую картину можно увидеть только в горах краснодарского края, да, я вот там бывал и поэтому могу точно сказать: всякое бывает, но не всякое можно забыть или хотя бы развидеть", "3", "4"],
                "answer": "4",
                "balls": 1
            },
            {
                "question": "question2",
                "type": 1,
                "variants_of_answer": ["1", "2", "3", "4"],
                "answer": "3",
                "balls": 1
            }
        ]
    } for i in range(4)]
    return testss 