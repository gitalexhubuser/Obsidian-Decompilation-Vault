---
offset: "0x008786e0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008786e0 — `SESound_SetAttachCustomDSPChainCallback`

- **Адрес (Offset):** `0x008786e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008786e0
void SESound::SetAttachCustomDSPChainCallback(void (*callback)(FMOD::Channel*, char*), const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008786e0 в IDA Pro / Ghidra
