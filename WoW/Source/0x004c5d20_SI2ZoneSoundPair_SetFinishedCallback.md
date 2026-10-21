---
offset: "0x004c5d20"
module: "WoW/Source"
file: "WoW/Source/SoundInterface/SoundInterface2.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004c5d20 — `SI2ZoneSoundPair_SetFinishedCallback`

- **Адрес (Offset):** `0x004c5d20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/SoundInterface/SoundInterface2.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004c5d20
void SI2ZoneSoundPair::SetFinishedCallback(void (*callback)(SESound*, void*), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004c5d20 в IDA Pro / Ghidra
