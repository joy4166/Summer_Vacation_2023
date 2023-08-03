def find_real_dwarf(dwarf_height):
    real_list = []
    for i in range(9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 9):
                        for n in range(m + 1, 9):
                            for o in range(n + 1, 9):
                                if dwarf_height[i] + dwarf_height[j] + dwarf_height[k] + dwarf_height[l] + dwarf_height[
                                    m] + dwarf_height[n] + dwarf_height[o] == 100:
                                    real_list.append(dwarf_height[i])
                                    real_list.append(dwarf_height[j])
                                    real_list.append(dwarf_height[k])
                                    real_list.append(dwarf_height[l])
                                    real_list.append(dwarf_height[m])
                                    real_list.append(dwarf_height[n])
                                    real_list.append(dwarf_height[o])
                                    real_list.sort()
                                    return real_list


dwarf_height = []
for _ in range(9):
    dwarf_height.append(int(input()))

real_list = find_real_dwarf(dwarf_height)
for i in range(7):
    print(real_list[i])