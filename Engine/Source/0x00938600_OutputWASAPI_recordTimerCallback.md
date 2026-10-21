---
offset: "0x00938600"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00938600 — `OutputWASAPI_recordTimerCallback`

- **Адрес (Offset):** `0x00938600`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00938600
void CALLBACK OutputWASAPI::recordTimerCallback(UINT uTimerID, UINT uMsg, DWORD_PTR dwUser, DWORD_PTR dw1, DWORD_PTR dw2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00938600 в IDA Pro / Ghidra
