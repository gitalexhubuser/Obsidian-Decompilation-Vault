---
offset: "0x009190a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_fft.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009190a0 — `DSPFFT_getSpectrum`

- **Адрес (Offset):** `0x009190a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_fft.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009190a0
FMOD_RESULT DSPFFT::getSpectrum(float *pcmbuffer, unsigned int pcmposition, unsigned int pcmlength, float *spectrum, int length, int channel, int numchannels, FMOD_DSP_FFT_WINDOW windowtype)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009190a0 в IDA Pro / Ghidra
