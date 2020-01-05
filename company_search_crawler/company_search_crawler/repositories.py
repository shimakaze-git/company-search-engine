import csv


class ScrapyCompanySearchRepository:
    def __init__(self):
        super().__init__()

        self.output_csv = "./data.csv"
        self.datas = []
        self.columns_name = []

    def execute(self, item):

        columns = []
        for idx in item:
            columns.append(item[idx])

        self.datas.append(columns)
        self.columns_name = [name for name in item]

    def save(self):

        with open(self.output_csv, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.columns_name)

            for data in self.datas:
                writer.writerow(data)
