---
offset: "0x00939c30"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00939c30 — `OutputWinMM_recordCallback`

- **Адрес (Offset):** `0x00939c30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00939c30
void CALLBACK OutputWinMM::recordCallback(HWAVEIN hwi, UINT uMsg, DWORD_PTR dwInstance, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00939c30 в IDA Pro / Ghidra
