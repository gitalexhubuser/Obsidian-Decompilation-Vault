---
offset: "0x004c6a40"
module: "WoW/Source"
file: "WoW/Source/SoundInterface/SoundInterface2.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004c6a40 — `SI2_PlaySoundKit`

- **Адрес (Offset):** `0x004c6a40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/SoundInterface/SoundInterface2.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004c6a40
int32_t SI2::PlaySoundKit(int32_t soundKitId, const C3Vector* position, SE2SoundKitObject* object, SE2SoundKitProperties* properties, uint32_t advancedId, uint32_t* soundId, int32_t checkDistance, int32_t keepPlaying) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004c6a40 в IDA Pro / Ghidra
