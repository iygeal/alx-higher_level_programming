  @classmethod
   def save_to_file_csv(cls, list_objs):
        """Serializes and saves to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV file"""
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = Rectangle(int(row[1]), int(row[2]), int(
                            row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = Square(int(row[1]), int(
                            row[2]), int(row[3]), int(row[0]))
                    obj_list.append(obj)
        except FileNotFoundError:
            pass
        return obj_list

