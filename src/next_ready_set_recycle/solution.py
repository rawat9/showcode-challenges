class NextSustainability:
    def percentage_recycled(self, product, material_information):
        hmap = {}
        total = 0
        materialOrRecycled = material_information[0]

        try:
            # is recycled
            product, args = materialOrRecycled.split("-")
            recycled = args.strip()
            percentage, _ = recycled.split(" ")

            return round(float(percentage[:-1]))

        except ValueError:
            # is material
            product, *args = materialOrRecycled.split(":")
            material = args[0].strip()
            arr = material.split(" ")
            for i in range(len(arr) - 1):
                if arr[i].endswith("%"):
                    hmap[arr[i + 1].lower().strip()] = arr[i][:-1]

        for info in material_information[1:]:
            mat, args = info.split("-")
            recycled = args.strip()
            percentage, _ = recycled.split(" ")

            amt = self.calc_percentage(
                float(hmap[mat.strip().lower()]), float(percentage[:-1])
            )

            total += amt

        return round(total)

    def calc_percentage(self, p1, p2):
        return (p1 * p2) / 100
