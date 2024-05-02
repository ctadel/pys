class Solution:
    def get_best_appartment(self, blocks, reqs):

        agg_blocks = []
        best_distance = float('inf')
        value_location = None, None

        def check_distance(field, cursor, increment):
            if cursor not in range(len(blocks)):
                return float('inf')

            if blocks[cursor][field]:
                return 0
            else:
                return 1 + check_distance(field, cursor+increment, increment)


        for index in range(len(blocks)):
            distances = {}
            for field in reqs:
                distances[field] = min(
                        check_distance(field, index, 1),
                        check_distance(field, index, -1)
                    )
            if max(distances.values()) < best_distance:
                best_distance = max(distances.values())
                value_location = distances, index

            agg_blocks.append(distances)

        return value_location

    def sort_build_array(self, data:list[list]):
        def calculate_percentage(array:list):
            fails = 0
            for i in array[::-1]:
                if i: break
                fails += 1
            return (len(array)-fails)/len(array)*100
        return sorted(data, key=lambda array:calculate_percentage(array), reverse=True)

blocks =[
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

reqs = ['gym', 'school', 'store']

data = [
        [True, True, True, False, False],
        [True, True, True, True, False],
        [True, True, True, True, True, True, False, False, False],
        [True, True, True, True, True, True, True, True, True, True, True, True, False, False],
        [True, False],
        [True, True, True, True, False, False]
    ]

response = Solution().get_best_appartment(blocks, reqs)
print(response)

response = Solution().sort_build_array(data)
for r in response:
    print(len([x for x in r if x])/len(r)*100, end = '\t')
    print(r)
