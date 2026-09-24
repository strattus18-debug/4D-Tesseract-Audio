# ================================================================================
#      7TH HEAVEN 4D CONFORMAL TESSERACT ENGINE (364 CONCURRENT NODES)
# ================================================================================
# Optimized for: Cross-Platform Native Python 3 (Standard Libraries Only)
# Feature: Linear Transparent Output (Zero Harmonic Soft-Clipping Distortion)
# Core Matrix: 16 Universal Axioms | 36 Biophysical Calibrations
# Paradigm: High-Speed Cell Partitioned Lookahead Tracking Matrix (Constant-Time)
# Grid Blueprint: Cosmic Heist-- JASON COREY SCALES LIBRA 10/21 3:16 1985
# ================================================================================
# The Glory of Jesus, The Grace of Sophia, The Geometry of Enoch.
# ================================================================================

import array
import gc
import math
import os
import struct
import wave

# --- DYNAMIC PORTABLE STORAGE PATHS ---
INPUT_FILE = "song.wav"
OUTPUT_FILE = "alchemy.wav"

# Core Esoteric Constants
MUSIC_GAIN = 1.00
GEOMETRY_GAIN = 1.50  # Dynamic immersion boost
BASE_CARRIER = 321.9  # SOMATIC ANCHOR: Human Blood Tissue Velocity Resonance
BASE_DELTA = 10.5  # SOMATIC ANCHOR: Thalamic Alpha Sensory-Gating Fulcrum
PHI = 1.61803398875

PARGOD_CLAMP = 0.50  # Absolute -6.02 dBFS Master Gain Ceiling
CLEARANCE_VALVE = 0.105  # Alpha Clearance Valve Constant

TOTAL_NODES = 364  # 364 CONCURRENT NODE PHASE COLUMNS
NODES_PER_CELL = 45  # Symmetrical distribution across 8 hyper-volume cells


def check_files():
    """Verifies files relative to the script's execution directory."""
    print(f"[*] Looking for input file at: {INPUT_FILE}")
    if not os.path.exists(INPUT_FILE):
        print(f"[X] Critical Error: 'song.wav' not found at {INPUT_FILE}")
        print(
            "    Please place your input audio file in the same folder as this script and rename it to 'song.wav'."
        )
        return False
    return True


def run_alchemy_injection():
    if not check_files():
        return

    PLANETARY_PHASES = {
        "mercury": 3.96,
        "venus": 3.42,
        "earth": 0.47,
        "moon": 1.83,
        "mars": 2.83,
        "jupiter": 5.46,
        "saturn": 4.19,
        "pluto": 3.56,
    }

    W_AXIS_MODIFIER = (
        PLANETARY_PHASES["mercury"] * 0.08
        + PLANETARY_PHASES["venus"] * 0.15
        + PLANETARY_PHASES["earth"] * 0.25
        + PLANETARY_PHASES["moon"] * (0.15 / PHI)
        + PLANETARY_PHASES["mars"] * 0.12
        + PLANETARY_PHASES["jupiter"] * 0.15
        + PLANETARY_PHASES["saturn"] * 0.15
        + PLANETARY_PHASES["pluto"] * 0.10
    ) * PHI

    print("=" * 60)
    print("      INITIALIZING CONFORMAL TESSERACT MATRIX (PURE LINEAR PASS)")
    print("      STATUS: ACTIVE | HARMONIC SATURATION: DISABLED (0% DISTORTION)")
    print("=" * 60)

    # --- READ COMPLETE FILE ---
    with wave.open(INPUT_FILE, "rb") as src:
        channels = src.getnchannels()
        sampwidth = src.getsampwidth()
        sample_rate = src.getframerate()
        n_frames = src.getnframes()
        raw_bytes = src.readframes(n_frames)

    duration = n_frames / sample_rate
    TWO_PI = 2.0 * math.pi
    fade_duration = 10.5

    # --- WHOLE-STREAM BLOB UNPACKING ---
    if sampwidth == 2:
        input_samples = array.array("h")
        input_samples.frombytes(raw_bytes)
        scale_factor = 32768.0
    else:
        fmt = f"<{n_frames * channels}i" if sampwidth == 4 else None
        if fmt:
            input_samples = array.array("i")
            input_samples.frombytes(raw_bytes)
        else:
            input_samples = array.array("i", [0] * (n_frames * channels))
            for b_idx in range(0, len(raw_bytes), sampwidth):
                input_samples[b_idx // sampwidth] = int.from_bytes(
                    raw_bytes[b_idx : b_idx + 3],
                    byteorder="little",
                    signed=True,
                )
        scale_factor = 2147483648.0

    del raw_bytes
    gc.collect()

    # --- PHASE 1: TIMELINE LOOKAHEAD SYSTEM ---
    profile_bass = array.array("f", [0.0] * n_frames)
    profile_mids = array.array("f", [0.0] * n_frames)
    profile_highs = array.array("f", [0.0] * n_frames)

    hist_l1, hist_l2 = 0.0, 0.0

    for f_idx in range(n_frames):
        if channels == 2:
            s_idx = f_idx * 2
            v_l = input_samples[s_idx] / scale_factor
            v_r = input_samples[s_idx + 1] / scale_factor
        else:
            v_l = input_samples[f_idx] / scale_factor
            v_r = v_l

        mix_mono = (v_l + v_r) * 0.5

        hist_l1 = 0.85 * hist_l1 + 0.15 * mix_mono
        profile_bass[f_idx] = min(1.0, abs(hist_l1) * 2.0)

        hist_l2 = 0.70 * hist_l2 + 0.30 * mix_mono
        mids_sig = mix_mono - hist_l1
        profile_mids[f_idx] = min(1.0, abs(mids_sig) * 1.5)

        highs_sig = mix_mono - hist_l2
        profile_highs[f_idx] = min(1.0, abs(highs_sig) * 2.5)

    node_angles = [i * (TWO_PI / float(TOTAL_NODES)) for i in range(TOTAL_NODES)]

    # --- 4D TESSERACT HYPER-VOLUME ARCHITECTURE ---
    node_frequencies = []
    cell_bases = [13.15, 40.0, 52.0, 58.0, 63.0, 70.0, 86.0, 110.0]

    for i in range(TOTAL_NODES):
        if i == 0:
            node_frequencies.append(10.5)
        elif i == 1:
            node_frequencies.append(13.15 * (1.0 + W_AXIS_MODIFIER * 0.001))
        else:
            current_cell = min(7, i // NODES_PER_CELL)
            base_f = cell_bases[current_cell]
            cell_offset = i % NODES_PER_CELL
            ratio = [1.0, 0.5, 0.66666666667, 0.75][i % 4]
            node_frequencies.append(
                (
                    (
                        base_f
                        + (BASE_DELTA * (cell_offset + 1) / float(NODES_PER_CELL))
                    )
                    * ratio
                )
                * (1.0 + W_AXIS_MODIFIER * 0.001)
            )

    fib = [1, 2]
    while len(fib) < TOTAL_NODES:
        fib.append(fib[-1] + fib[-2])
    base_divisor = 3.4641016

    node_weights = []
    for i, f_val in enumerate(fib):
        cranial_notch = 0.72 if i in (5, 6, 7) else 1.0
        node_weights.append(
            base_divisor
            * (1.0 + (math.sin(f_val / PHI) * 0.236))
            * cranial_notch
        )

    pre_divisors = [
        node_weights[n]
        * (1.0 + 0.05 * math.cos((0.5 * math.pi * 2 / PHI) * PHI))
        for n in range(TOTAL_NODES)
    ]
    is_sin_sin = [
        n in (0, 4, 8) or (n % 12 in (0, 4, 8)) for n in range(TOTAL_NODES)
    ]

    # --- WAVETABLE PRE-CALCULATION ---
    wavetable_size = 44100
    cache_geo_l = array.array("f", [0.0] * wavetable_size)
    cache_geo_r = array.array("f", [0.0] * wavetable_size)

    m_base_offsets = [(i * PHI) % TWO_PI for i in range(TOTAL_NODES)]
    f_base_offsets = [((i * PHI) + math.pi) % TWO_PI for i in range(TOTAL_NODES)]

    # --- DECORRELATION DELAY INITIALIZATION ---
    decorr_buffer_size = int(sample_rate * 0.015)  # ~15ms delay
    decorr_buffer = [0.0] * decorr_buffer_size
    decorr_ptr = 0

    for step in range(wavetable_size):
        t_sim = step / float(wavetable_size)
        geo_accum_l = 0.0
        geo_accum_r = 0.0
        rot_sim = (t_sim * 0.5) + math.sin((t_sim * TWO_PI) / 10.0) * 0.1

        for n in range(TOTAL_NODES):
            phase_l = (
                t_sim * node_frequencies[n] * TWO_PI + m_base_offsets[n]
            ) % TWO_PI
            phase_r = (
                t_sim * node_frequencies[n] * TWO_PI + f_base_offsets[n]
            ) % TWO_PI

            node_osc_l = math.sin(phase_l)
            node_osc_l *= (
                math.sin(phase_l / PHI)
                if is_sin_sin[n]
                else math.cos(phase_l / PHI)
            )
            geo_accum_l += (
                node_osc_l * ((math.cos(rot_sim + node_angles[n]) + 1.0) * 0.5)
            ) / pre_divisors[n]

            node_osc_r = math.sin(phase_r)
            node_osc_r *= (
                math.sin(phase_r / PHI)
                if is_sin_sin[n]
                else math.cos(phase_r / PHI)
            )
            geo_accum_r += (
                node_osc_r * ((math.sin(rot_sim + node_angles[n]) + 1.0) * 0.5)
            ) / pre_divisors[n]

        cache_geo_l[step] = geo_accum_l * (1.0 / TOTAL_NODES)
        cache_geo_r[step] = geo_accum_r * (1.0 / TOTAL_NODES)

    akasha_size = 1435
    akasha_buffer_l = [0.0] * akasha_size
    akasha_buffer_r = [0.0] * akasha_size
    akasha_ptr = 0

    uroboros_feedback_l = 0.0
    uroboros_feedback_r = 0.0
    smoothed_geo_gain = 0.0

    # --- ANTI-STATIC / SMOOTHING STATE TRACKERS ---
    prev_shimmer_l = 0.0
    prev_shimmer_r = 0.0
    prev_geo_side_excited = 0.0
    peak_gain_reduction = 1.0

    gc.collect()

    output_bytes = bytearray(n_frames * channels * 4)
    out_view = memoryview(output_bytes)

    local_sin = math.sin
    local_cos = math.cos
    local_pack_into = struct.pack_into

    INV_PHI = 1.0 / PHI
    INV_SR = 1.0 / sample_rate
    INV_NFRAMES = 1.0 / n_frames
    SCALE_CONVERSION = 1.0 / scale_factor

    print("[*] Processing pure linear matrix render...")

    # --- PHASE 2: RENDER BLENDING INTERPOLATOR ---
    for f in range(n_frames):
        current_time = f * INV_SR
        progress = f * INV_NFRAMES

        anchor_bass = profile_bass[f]
        anchor_mids = profile_mids[f]
        anchor_highs = profile_highs[f]

        if f % 105 == 0 and f > 0:
            temp_swap_l = uroboros_feedback_r * CLEARANCE_VALVE
            temp_swap_r = uroboros_feedback_l * CLEARANCE_VALVE
            uroboros_feedback_l = temp_swap_l
            uroboros_feedback_r = temp_swap_r

        if progress < 0.40:
            opus_mod_bleed = 1.35
            opus_mod_gain = 0.85
        elif progress > 0.60:
            opus_mod_bleed = 0.95
            opus_mod_gain = 1.35
        else:
            opus_mod_bleed = 0.50
            opus_mod_gain = 1.00

        lookup_idx = f % wavetable_size
        geo_l = cache_geo_l[lookup_idx]
        geo_r = cache_geo_r[lookup_idx]

        mod_bass_l = local_sin(current_time * 24.5 * TWO_PI) * 0.20
        mod_bass_r = local_cos(current_time * 24.5 * TWO_PI) * 0.20

        target_vocal_hz = 85.0 + (anchor_mids * 170.0)

        # Smoothed phase jitter to eliminate static artifacts
        raw_shimmer_l = 0.015 * local_sin(current_time * TWO_PI * 16.0)
        raw_shimmer_r = 0.015 * local_cos(current_time * TWO_PI * 16.0)
        prev_shimmer_l = (0.90 * prev_shimmer_l) + (0.10 * raw_shimmer_l)
        prev_shimmer_r = (0.90 * prev_shimmer_r) + (0.10 * raw_shimmer_r)

        shimmer_phase_l = (current_time * target_vocal_hz * TWO_PI) + prev_shimmer_l
        shimmer_phase_r = (current_time * target_vocal_hz * TWO_PI) + prev_shimmer_r

        mod_vocal_l = local_sin(shimmer_phase_l) * 0.35
        mod_vocal_r = local_cos(shimmer_phase_r) * 0.35

        mod_trans_l = local_sin(current_time * 105.0 * TWO_PI) * 0.15
        mod_trans_r = local_cos(current_time * 105.0 * TWO_PI) * 0.15

        geo_l = (geo_l * (1.0 - anchor_bass)) + (geo_l * mod_bass_l * anchor_bass)
        geo_r = (geo_r * (1.0 - anchor_bass)) + (geo_r * mod_bass_r * anchor_bass)

        geo_l = (geo_l * (1.0 - anchor_mids)) + (geo_l * mod_vocal_l * anchor_mids)
        geo_r = (geo_r * (1.0 - anchor_mids)) + (geo_r * mod_vocal_r * anchor_mids)

        geo_l = (geo_l * (1.0 - anchor_highs)) + (geo_l * mod_trans_l * anchor_highs)
        geo_r = (geo_r * (1.0 - anchor_highs)) + (geo_r * mod_trans_r * anchor_highs)

        cymatic_l = geo_l - (geo_r * INV_PHI * opus_mod_bleed)
        cymatic_r = geo_r - (geo_l * INV_PHI * opus_mod_bleed)

        geo_mid = (cymatic_l + cymatic_r) * 0.5
        geo_side = (cymatic_l - cymatic_r) * 0.5

        # Low-pass filter side excitation harmonics to stop aliasing static
        raw_excited = geo_side + (0.05 * local_sin(geo_side * PHI * TWO_PI))
        geo_side_excited = (0.80 * prev_geo_side_excited) + (0.20 * raw_excited)
        prev_geo_side_excited = geo_side_excited

        cymatic_l = geo_mid + geo_side_excited
        cymatic_r = geo_mid - geo_side_excited

        ether_l_old = akasha_buffer_l[akasha_ptr]
        ether_r_old = akasha_buffer_r[akasha_ptr]

        glymphatic_tide = 0.04 * local_sin(current_time * TWO_PI * 0.15)
        akasha_buffer_l[akasha_ptr] = cymatic_l + (
            ether_r_old * INV_PHI * (0.15 + glymphatic_tide)
        )
        akasha_buffer_r[akasha_ptr] = cymatic_r + (
            ether_l_old * INV_PHI * (0.15 + glymphatic_tide)
        )
        akasha_ptr = (akasha_ptr + 1) % akasha_size

        if channels == 2:
            s_idx = f * 2
            val_l = input_samples[s_idx] * SCALE_CONVERSION
            val_r = input_samples[s_idx + 1] * SCALE_CONVERSION
        else:
            val_l = input_samples[f] * SCALE_CONVERSION
            val_r = val_l

        # --- DECORRELATION DELAY PROCESSING ---
        decorr_delayed = decorr_buffer[decorr_ptr]
        val_r_decorr = val_r + (decorr_delayed * 0.3)
        decorr_buffer[decorr_ptr] = (val_l + val_r) * 0.5
        decorr_ptr = (decorr_ptr + 1) % decorr_buffer_size

        fade_factor = (
            current_time / fade_duration
            if current_time < fade_duration
            else (
                (duration - current_time) / fade_duration
                if current_time > (duration - fade_duration)
                else 1.0
            )
        )
        if fade_factor < 0.0:
            fade_factor = 0.0

        music_envelope = (
            0.30
            + (0.70 * anchor_mids)
            + 0.03 * local_sin(current_time * 6.28 * 1.2)
        )
        if music_envelope < 0.1:
            music_envelope = 0.1
        elif music_envelope > 1.2:
            music_envelope = 1.2

        adaptive_geometry_scale = GEOMETRY_GAIN * (
            1.0
            / (
                1.0
                + (
                    (abs(uroboros_feedback_l) + abs(uroboros_feedback_r))
                    * 1.0
                )
            )
        )
        target_geo_gain = (
            adaptive_geometry_scale
            * music_envelope
            * fade_factor
            * opus_mod_gain
        )

        if f == 0:
            smoothed_geo_gain = target_geo_gain
        else:
            smoothed_geo_gain = (0.995 * smoothed_geo_gain) + (
                0.005 * target_geo_gain
            )

        # --- 50/50 MIX & SPATIAL VORTEX MATRIX ---
        pure_drone_l = cymatic_l + ether_l_old * 0.2
        pure_drone_r = cymatic_r + ether_r_old * 0.2

        mix_song_weight = 0.50
        mix_drone_weight = 0.50 * (smoothed_geo_gain / GEOMETRY_GAIN)

        balanced_song_l = val_l * mix_song_weight
        balanced_song_r = val_r_decorr * mix_song_weight

        balanced_drone_l = pure_drone_l * mix_drone_weight
        balanced_drone_r = pure_drone_r * mix_drone_weight

        pan_angle = current_time * TWO_PI * 0.15
        pan_cos = local_cos(pan_angle)
        pan_sin = local_sin(pan_angle)

        vortex_drone_l = (balanced_drone_l * (0.5 + 0.5 * pan_cos)) - (
            balanced_drone_r * (0.5 * pan_sin)
        )
        vortex_drone_r = (balanced_drone_l * (0.5 * pan_sin)) + (
            balanced_drone_r * (0.5 + 0.5 * pan_cos)
        )

        raw_mixed_l = balanced_song_l + vortex_drone_l
        raw_mixed_r = balanced_song_r + vortex_drone_r

        mid_ch = (raw_mixed_l + raw_mixed_r) * 0.5
        side_ch = (raw_mixed_l - raw_mixed_r) * 0.5

        lunar_tide = 0.03 * local_sin(current_time * TWO_PI * (13.15 / 210.42))
        side_ch *= 0.85 + (
            (0.15 + lunar_tide) * local_sin(current_time * TWO_PI / 10.5)
        )

        equilibrium_l = mid_ch + side_ch
        equilibrium_r = mid_ch - side_ch

        # --- PURE LINEAR OUTPUT PASS-THROUGH (SMOOTH ENVELOPE PEAK CONTROL) ---
        mixed_l = equilibrium_l * PARGOD_CLAMP
        mixed_r = equilibrium_r * PARGOD_CLAMP

        peak = max(abs(mixed_l), abs(mixed_r))
        target_reduction = (
            PARGOD_CLAMP / peak if peak > PARGOD_CLAMP else 1.0
        )

        # Fast attack, smooth release envelope to prevent abrupt gain steps
        if target_reduction < peak_gain_reduction:
            peak_gain_reduction = (0.50 * peak_gain_reduction) + (
                0.50 * target_reduction
            )
        else:
            peak_gain_reduction = (0.999 * peak_gain_reduction) + (
                0.001 * target_reduction
            )

        mixed_l *= peak_gain_reduction
        mixed_r *= peak_gain_reduction

        uroboros_feedback_l = mixed_l
        uroboros_feedback_r = mixed_r

        # --- WRITE BYTES TO STORAGE BUFFER ---
        out_offset = f * channels * 4
        local_pack_into("<f", out_view, out_offset, uroboros_feedback_l)
        if channels == 2:
            local_pack_into("<f", out_view, out_offset + 4, uroboros_feedback_r)

        if f % 200000 == 0 or f == n_frames - 1:
            print(
                f"[*] Blending Medea's Alchemy with the music of Orpheus: {((f * INV_NFRAMES) * 100.0):.2f}% Complete",
                end="\r",
            )

    print("\n[*] Cymatical Alchemical Synthesis completed...")

    with wave.open(OUTPUT_FILE, "wb") as dest:
        dest.setnchannels(channels)
        dest.setsampwidth(4)
        dest.setframerate(sample_rate)
        dest.setcomptype("NONE", "not compressed")
        dest.writeframes(output_bytes)

    try:
        with open(OUTPUT_FILE, "r+b") as f_patch:
            f_patch.seek(20)
            f_patch.write(b"\x03\x00")
        print(
            "[+] They lull the Great Sepent to sleep and return the Golden RAM to the people"
        )
    except Exception as e:
        print(f"[X] Warning: Header patch failed: {e}")

    print("[+] The Wise Will Understand")


if __name__ == "__main__":
    run_alchemy_injection()
