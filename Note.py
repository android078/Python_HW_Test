class Note:
    units_num = 0

    def __init__(self, id, title, body, date_mark, time_mark):
        Note.units_num += 1

        self.title = title
        self.id = id
        self.date_mark = date_mark
        self.time_mark = time_mark
        self.body = body

    def date_time(self):
        return self.datemark + " (" + self.time_mark + ")"