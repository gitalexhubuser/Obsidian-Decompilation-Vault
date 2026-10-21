---
offset: "0x006b6630"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b6630 — `FriendListNameCallback`

- **Адрес (Offset):** `0x006b6630`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b6630
void FriendListNameCallback(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b6630 в IDA Pro / Ghidra
