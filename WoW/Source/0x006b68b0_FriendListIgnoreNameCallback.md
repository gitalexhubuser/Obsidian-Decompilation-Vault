---
offset: "0x006b68b0"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b68b0 — `FriendListIgnoreNameCallback`

- **Адрес (Offset):** `0x006b68b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b68b0
void FriendListIgnoreNameCallback(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b68b0 в IDA Pro / Ghidra
