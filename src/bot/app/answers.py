from enum import Enum


class Answers(str, Enum):
    REQUEST_ID = 'пришлите id вашего обращения для подсписи на уведомления об изменениях'
    ACCEPTED_SUBSCRIBE = 'Вы будуете получать уведомления об изменениях  в ашем обращении'
    NOT_FOUND_ID = 'id не найден'