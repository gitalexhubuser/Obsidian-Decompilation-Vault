---
offset: "0x0076db30"
module: "WoW/Source"
file: "WoW/Source/Game/GameTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0076db30 — `CGameTime_GameTimeRegisterCallback`

- **Адрес (Offset):** `0x0076db30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0076db30
TIMESTAMPCALLBACK* CGameTime::GameTimeRegisterCallback(const WowTime* time, void (__stdcall* callback)(CGameTime* time, void* param), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0076db30 в IDA Pro / Ghidra
