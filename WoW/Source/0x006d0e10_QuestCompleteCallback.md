---
offset: "0x006d0e10"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Player_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006d0e10 — `QuestCompleteCallback`

- **Адрес (Offset):** `0x006d0e10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Player_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006d0e10
static void QuestCompleteCallback(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006d0e10 в IDA Pro / Ghidra
