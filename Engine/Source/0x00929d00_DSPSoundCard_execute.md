---
offset: "0x00929d00"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_soundcard.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00929d00 — `DSPSoundCard_execute`

- **Адрес (Offset):** `0x00929d00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_soundcard.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00929d00
FMOD_RESULT DSPSoundCard::execute(void *inbuffer, void **outbuffer, unsigned int *length, int inchannels, int *outchannels, FMOD_SPEAKERMODE speakermode)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00929d00 в IDA Pro / Ghidra
