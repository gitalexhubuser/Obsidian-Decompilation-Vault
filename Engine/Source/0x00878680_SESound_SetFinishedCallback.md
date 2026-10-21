---
offset: "0x00878680"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00878680 — `SESound_SetFinishedCallback`

- **Адрес (Offset):** `0x00878680`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00878680
void SESound::SetFinishedCallback(void (*callback)(SESound*, void*), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00878680 в IDA Pro / Ghidra
