---
offset: "0x007e6dc0"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/WorldText.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e6dc0 — `WorldTextCreate`

- **Адрес (Offset):** `0x007e6dc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/WorldText.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e6dc0
WORLDTEXTSTRING* WorldTextCreate(uint32_t type, const C3Vector& position, const char* text, const CImVector* color, const int32_t* pvpRank) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e6dc0 в IDA Pro / Ghidra
