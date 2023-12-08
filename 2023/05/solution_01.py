inputfile = "input.txt"
f = open(inputfile, "r")

# GOAL: Find the lowest location number that corresponds to any of the initial seed numbers

# The input lists the seeds to be planted, what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil etc.

# Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category:
#   soil 123 and fertilizer 123 aren't necessarily related to each other

# Example:

    # seeds: 79 14 55 13

    # seed-to-soil map:         <-- source: seed, dest: soil
    # 50 98 2                   <-- dest (soil): 50, source (seed): 98, range 2
    # 52 50 48                  <-- dest (soil): 52, source (seed): 50, range 48

    # soil-to-fertilizer map:   <-- source: soil, dest: fertilizer
    # 0 15 37                   <-- dest (fertilizer): 0, source (soil): 15 range 37
    # 37 52 2                   <-- dest (fertilizer): 37, source (soil): 52 range 2
    # 39 0 15                   <-- dest (fertilizer): 39, source (soil): 0 range 15

    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4

    # water-to-light map:
    # 88 18 7
    # 18 25 70

    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13

    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69

    # humidity-to-location map:
    # 60 56 37
    # 56 93 4

# The maps which describe how to convert numbers from a source category into numbers in a destination category. 
# The section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). 

# The maps describe ranges of numbers that can be converted. 
# Each line contains three numbers: 
#   destination range start
#   source range start
#   range length

# Example seed-to-soil map line:

# 50 98 2           # destination (soil) range start 50, source (seed) range start 98, range length 2. 
                    # i.e. seed 98 corresponds to soil 50 and seed 99 corresponds to soil 51.

# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

# So, the entire list of seed numbers and their corresponding soil numbers looks like this:

# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

# With this map, you can look up the soil number required for each initial seed number

# The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

#     Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#     Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#     Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#     Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# So, the lowest location number in this example is 35.

mappings=[]

# Examples of mappings elements:
# mapping_range={'source_start':0,'dest_start':0,'range':0}
# mapping={'source':'seed','dest':'soil','mapping_ranges':[mapping_ranges]}

processing_mappings=False

for line in f:
    line_text=line.split('\n')[0]               # get rid of the newline character
    if line_text.find('seeds:')==0:                  # i.e. line begins "seeds:"
        seed_list=line_text.split('seeds: ')[1].split(' ')      # list of seeds is the space-separated list that appears after "seeds: "
    elif line.find('map:')>-1:
        # begin to process mapping
        processing_mappings=True
        mapping_name=line_text.split(' map:')[0]
        source_type=mapping_name.split('-to-')[0]
        dest_type=mapping_name.split('-to-')[1]
        mapping_ranges=[]
        # print('source_type:',source_type)
        # print('dest_type:',dest_type)
    elif line_text=='':
        if processing_mappings:
            # we've finished processing the previous mapping and we're starting to process a mapping.
            # print('finished processing mapping')
            mapping={'source':source_type,'dest':dest_type,'mapping_ranges':mapping_ranges}
            mappings.append(mapping)
    else:
        # line is a list of 3 numbers representing the mapping
        dest_start=int(line_text.split(' ')[0])
        source_start=int(line_text.split(' ')[1])
        range=int(line_text.split(' ')[2])
        source_end=source_start+(range-1)
        offset=dest_start-source_start
        mapping_range={'source_start':source_start,'source_end':source_end,'offset':offset}
        mapping_ranges.append(mapping_range)
        # print('source_start: ',source_start, 'source_end: ', source_end)
        # print('offset: ',offset)
# finished processing the final mapping
# print('finished processing mapping')
mapping={'source':source_type,'dest':dest_type,'mapping_ranges':mapping_ranges}
mappings.append(mapping)

def traverse_mappings(source_type, source_val):
    # print('executing traverse_mappings(',source_type,',',source_val,')')
    mapping = next(mapping for mapping in mappings if mapping['source'] == source_type)
    # print(mapping)
    # calculate new value
    mapping_ranges=mapping['mapping_ranges']
    dest_val=source_val
    for range in mapping_ranges:
        # print('start val of range:',range['source_start'],'end val of range:',range['source_end'], 'offset: ',range['offset'])
        if source_val >= range['source_start'] and source_val <= range['source_end']:
            dest_val=source_val+range['offset']
    dest_type=mapping['dest']
    return dest_val if dest_type == 'location' else traverse_mappings(dest_type, dest_val)

min_location=-1
min_location_seed=0

for seed in seed_list:
    location=traverse_mappings('seed', int(seed))
    # print('seed',seed,'maps to location',location)
    if min_location==-1 or location < min_location:
        min_location=location
        min_location_seed=seed

print(min_location)

f.close()