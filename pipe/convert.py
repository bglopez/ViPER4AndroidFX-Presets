import os
from pathlib import Path
from utils.create_directories import create_directories

# Path to Default Presets
default_m1_preset_file = Path('default_presets/default_m1.xml')
default_m2_preset_file = Path('default_presets/default_m2.xml')

def convert_presets(input_dir: Path, output_dir: Path) -> Path:
    """Convert any ViPER Preset XML to version 2.7.2+ compatible format."""
    print("Converting Presets ...")

    preset_converted_dir = output_dir/'preset-converted'
    create_directories([preset_converted_dir])

    # List all files in input directory
    for root, _, files in os.walk(input_dir):
        root = Path(root)

        # For each file
        for file in files:

            old_preset_file = root/file
            new_preset_file = preset_converted_dir/file
            # Select Default Preset file
            if (any(keyword in file.lower() for keyword in ['bluetooth', 'headset', 'usb'])):
                default_preset_file = default_m1_preset_file
            elif ('speaker' in file.lower()):
                default_preset_file = default_m2_preset_file
            else:
                print(f'\nCannot determine Preset type:\n{old_preset_file}')
                continue

            # Opening files to work with
            # Default Preset
            # Old Preset
            # New Preset
            with (
                open(default_preset_file, 'r') as default_preset,
                open(old_preset_file, 'r') as old_preset,
                open(new_preset_file, 'w') as new_preset
            ):

                default_preset = default_preset.read().splitlines()
                old_preset = old_preset.read().splitlines()

                # For each line of Default Preset
                for default_line in default_preset:
                    default_line = default_line.strip()

                    # Mode
                    # Master Switch -> Enabled
                    # Playback Gain -> Enabled
                    # Keep Master Limiter & Playback Gain values to ViPER defaults
                    if any(key in default_line for key in ('32775', '36868', '65586', '65587', '65588', '65565', '65566', '65567', '65568')):
                        if (('36868' in default_line) or ("65565" in default_line)):
                            new_preset.write(default_line.replace('false', 'true') + "\n")
                        else:
                            new_preset.write(default_line + "\n")

                    # FET Compressor
                    # ViPER DDC
                    # Spectrum Extension
                    # FIR Equalizer
                    # Convolver
                    # Field Surround
                    # Headphone Surround +
                    # Reverberation
                    # Dynamic System
                    # Tube Simulator (6N1J)
                    # ViPER Bass
                    # ViPER Clarity
                    # Auditory System Protection
                    # AnalogX
                    # Speaker Optimization
                    else:

                        # For each line of Old Preset
                        for old_line in old_preset:
                            old_line = old_line.strip()

                            # Keep Master Limiter & Playback Gain values to ViPER defaults

                            # # Master Limiter

                            # if ('65586' in default_line):
                            #     if (('65586' in old_line) or ('65608' in old_line)):
                            #         old_line = old_line.split('"')
                            #         if 21 < int(old_line[3]) :
                            #             # Normalizing to range of 0 - 21
                            #             old_line[3] = str([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200].index(int(old_line[3])))
                            #         old_line = '"'.join(old_line)
                            #         new_preset.write(old_line.replace('65608', '65586') + "\n")
                            #         break

                            # elif ('65588' in default_line):
                            #     if (('65588' in old_line) or ('65609' in old_line)):
                            #         old_line = old_line.split('"')
                            #         if 5 < int(old_line[3]) :
                            #             # Normalizing to range of 0 - 5
                            #             old_line[3] = str([30, 50, 70, 80, 90, 100].index(int(old_line[3])))
                            #         old_line = '"'.join(old_line)
                            #         new_preset.write(old_line.replace('65609', '65588') + "\n")
                            #         break

                            # # Playback Gain Control

                            # if (('65565' in default_line) and ('65604' in old_line)):
                            #     new_preset.write(old_line.replace('65604', '65565') + "\n")
                            #     break

                            # elif ('65566' in default_line):
                            #     if (('65566' in old_line) or ('65605' in old_line)):
                            #         old_line = old_line.split('"')
                            #         if 2 < int(old_line[3]) :
                            #             # Normalizing to range of 0 - 2
                            #             old_line[3] = str([50, 100, 300].index(int(old_line[3])))
                            #         old_line = '"'.join(old_line)
                            #         new_preset.write(old_line.replace('65605', '65566') + "\n")
                            #         break

                            # elif ('65567' in default_line):
                            #     if (('65567' in old_line) or ('65606' in old_line)):
                            #         old_line = old_line.split('"')
                            #         if 5 < int(old_line[3]) :
                            #             # Normalizing to range of 0 - 5
                            #             old_line[3] = str([30, 50, 70, 80, 90, 100].index(int(old_line[3])))
                            #         old_line = '"'.join(old_line)
                            #         new_preset.write(old_line.replace('65606', '65567') + "\n")
                            #         break

                            # elif ('65568' in default_line):
                            #     if (('65568' in old_line) or ('65607' in old_line)):
                            #         old_line = old_line.split('"')
                            #         if 10 < int(old_line[3]) :
                            #             # Normalizing to range of 0 - 10
                            #             old_line[3] = str([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 3000].index(int(old_line[3])))
                            #         old_line = '"'.join(old_line)
                            #         new_preset.write(old_line.replace('65607', '65568') + "\n")
                            #         break

                            # FET Compressor

                            if (('65610' in default_line) and ('65627' in old_line)):
                                new_preset.write(old_line.replace('65627', '65610') + "\n")
                                break

                            elif (('65611' in default_line) and ('65628' in old_line)):
                                new_preset.write(old_line.replace('65628', '65611') + "\n")
                                break

                            elif (('65612' in default_line) and ('65629' in old_line)):
                                new_preset.write(old_line.replace('65629', '65612') + "\n")
                                break

                            elif (('65613' in default_line) and ('65630' in old_line)):
                                new_preset.write(old_line.replace('65630', '65613') + "\n")
                                break

                            elif (('65614' in default_line) and ('65631' in old_line)):
                                new_preset.write(old_line.replace('65631', '65614') + "\n")
                                break

                            elif (('65615' in default_line) and ('65632' in old_line)):
                                new_preset.write(old_line.replace('65632', '65615') + "\n")
                                break

                            elif (('65616' in default_line) and ('65633' in old_line)):
                                new_preset.write(old_line.replace('65633', '65616') + "\n")
                                break

                            elif (('65617' in default_line) and ('65634' in old_line)):
                                new_preset.write(old_line.replace('65634', '65617') + "\n")
                                break

                            elif (('65618' in default_line) and ('65635' in old_line)):
                                new_preset.write(old_line.replace('65635', '65618') + "\n")
                                break

                            elif (('65619' in default_line) and ('65636' in old_line)):
                                new_preset.write(old_line.replace('65636', '65619') + "\n")
                                break

                            elif (('65620' in default_line) and ('65637' in old_line)):
                                new_preset.write(old_line.replace('65637', '65620') + "\n")
                                break

                            elif (('65621' in default_line) and ('65638' in old_line)):
                                new_preset.write(old_line.replace('65638', '65621') + "\n")
                                break

                            elif (('65622' in default_line) and ('65639' in old_line)):
                                new_preset.write(old_line.replace('65639', '65622') + "\n")
                                break

                            elif (('65623' in default_line) and ('65640' in old_line)):
                                new_preset.write(old_line.replace('65640', '65623') + "\n")
                                break

                            elif (('65624' in default_line) and ('65641' in old_line)):
                                new_preset.write(old_line.replace('65641', '65624') + "\n")
                                break

                            elif (('65625' in default_line) and ('65642' in old_line)):
                                new_preset.write(old_line.replace('65642', '65625') + "\n")
                                break

                            elif (('65626' in default_line) and ('65643' in old_line)):
                                new_preset.write(old_line.replace('65643', '65626') + "\n")
                                break

                            # FIR Equalizer

                            if (('65551' in default_line) and ('65595' in old_line)):
                                new_preset.write(old_line.replace('65595', '65551') + "\n")
                                break

                            elif (('65552' in default_line) and ('65596' in old_line)):
                                new_preset.write(old_line.replace('65596', '65552') + "\n")
                                break

                            # Convolver

                            if (('65538' in default_line) and ('65589' in old_line)):
                                new_preset.write(old_line.replace('65589', '65538') + "\n")
                                break

                            elif ('65540;65541;65542' in default_line):
                                if (('65540;65541;65542' in old_line) or ('65591;65592;65593' in old_line)):
                                    # Correcting '&' in Kernel(.irs) names
                                    old_line = (
                                        old_line
                                            .replace('></string>amp;', '&amp;')
                                            .replace('>Select impulse response file</string>amp;', '&amp;')
                                            .replace('Select impulse response file', '')
                                            .replace('Kernel', '')
                                            .replace('Choose Impulse Response', '')
                                            .replace('Selecione o arquivo de impulso de resposta', '')
                                    )
                                    new_preset.write(old_line.replace('65591;65592;65593', '65540;65541;65542') + "\n")
                                    break

                            elif (('65543' in default_line) and ('65594' in old_line)):
                                new_preset.write(old_line.replace('65594', '65543') + "\n")
                                break

                            # Reverberation

                            if (('65559' in default_line) and ('65597' in old_line)):
                                new_preset.write(old_line.replace('65597', '65559') + "\n")
                                break

                            elif ('65560' in default_line):
                                if (('65560' in old_line) or ('65598' in old_line)):
                                    old_line = old_line.split('"')
                                    if 10 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 10
                                        old_line[3] = str(int(int(old_line[3])/10))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line.replace('65598', '65560') + "\n")
                                    break

                            elif ('65561' in default_line):
                                if (('65561' in old_line) or ('65599' in old_line)):
                                    old_line = old_line.split('"')
                                    if 10 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 10
                                        old_line[3] = str(int(int(old_line[3])/10))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line.replace('65599', '65561') + "\n")
                                    break

                            elif (('65562' in default_line) and ('65600' in old_line)):
                                new_preset.write(old_line.replace('65600', '65562') + "\n")
                                break

                            elif (('65563' in default_line) and ('65601' in old_line)):
                                new_preset.write(old_line.replace('65601', '65563') + "\n")
                                break

                            elif (('65564' in default_line) and ('65602' in old_line)):
                                new_preset.write(old_line.replace('65602', '65564') + "\n")
                                break

                            # ViPER DDC
                            # Spectrum Extention
                            # Field Surround
                            # Differential Surround
                            # Headphone Surround +
                            # Dynamic System
                            # Tube Simulator (6N1J)
                            # ViPER Bass
                            # ViPER Clarity
                            # Auditory System Protection
                            # AnalogX
                            if (default_line[default_line.find('"')+1:default_line.find('"', default_line.find('"')+1)] == old_line[old_line.find('"')+1:old_line.find('"', old_line.find('"')+1)]):

                                # Field Surround

                                if ('65554;65556' in default_line):
                                    old_line = old_line.split('"')
                                    if 8 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 8
                                        old_line[3] = str(int((int(old_line[3])-120)/10))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                elif ('65555' in default_line):
                                    old_line = old_line.split('"')
                                    if 10 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 10
                                        old_line[3] = str(int((int(old_line[3])-120)/10))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                # Differential Surround

                                if ('65558' in default_line):
                                    old_line = old_line.split('"')
                                    if 19 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 19
                                        old_line[3] = str(int((int(old_line[3])/100)-1))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                # Dynamic System

                                if ('65573' in default_line):
                                    old_line = old_line.split('"')
                                    if 100 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 100
                                        old_line[3] = str(int((int(old_line[3])-100)/20))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                # ViPER Bass

                                if ('65576' in default_line):
                                    old_line = old_line.split('"')
                                    if 135 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 135
                                        old_line[3] = str(int(int(old_line[3])-15))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                elif ('65577' in default_line):
                                    old_line = old_line.split('"')
                                    if 11 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 11
                                        old_line[3] = str(int((int(old_line[3])-50)/50))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                # ViPER Clarity

                                if ('65580' in default_line):
                                    old_line = old_line.split('"')
                                    if 9 < int(old_line[3]) :
                                        # Normalizing to range of 0 - 9
                                        old_line[3] = str(int(int(old_line[3])/50))
                                    old_line = '"'.join(old_line)
                                    new_preset.write(old_line + "\n")
                                    break

                                # Remaining Features
                                new_preset.write(old_line + "\n")
                                break

                        # Speaker Optimization
                        else:
                            new_preset.write(default_line + "\n")

    return(preset_converted_dir)

if __name__ == "__main__":
    input_dir = Path('')
    output_dir = Path('')
    convert_presets(input_dir, output_dir)
