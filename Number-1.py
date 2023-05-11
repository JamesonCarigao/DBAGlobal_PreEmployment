arraySet = [5, 1, 4, 6, 7, 3, 5, 7, 3];

for arrayList in range(0, len(arraySet)):
    for arrayValue in range(arrayList + 1, len(arraySet)):
        if (arraySet[arrayList] == arraySet[arrayValue]):
            data = arraySet[arrayValue];
            print("Duplicate elements:", data);