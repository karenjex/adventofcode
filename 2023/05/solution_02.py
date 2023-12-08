inputfile = "input.txt"
f = open(inputfile, "r")

# NEED TO MAKE THE CODE (MUCH) MORE EFFICIENT - WORKS FOR THE TEST INPUT BUT NOT GOOD ENOUGH FOR THE MAIN INPUT

# GOAL: Find the lowest location number that corresponds to any of the initial seed numbers

# As for part 1 but the values on the initial seeds: line come in pairs. 
# Within each pair, the first value is the start of the range and the second value is the length of the range. 
# So, in the first line of the example (seeds: 79 14 55 13)

# The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. 
# The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

# In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. 
# So, the lowest location number is 46.

mappings=[]

# Examples of mappings elements:
# mapping_range={'source_start':0,'dest_start':0,'range':0}
# mapping={'source':'seed','dest':'soil','mapping_ranges':[mapping_ranges]}

processing_mappings=False

for line in f:
    line_text=line.split('\n')[0]               # get rid of the newline character
    if line_text.find('seeds:')==0:                  # i.e. line begins "seeds:"
        seed_ranges=line_text.split('seeds: ')[1].split(' ')      # list of seeds is the space-separated list that appears after "seeds: "
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
        map_range=int(line_text.split(' ')[2])
        source_end=source_start+(map_range-1)
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
    for map_range in mapping_ranges:
        # print('start val of range:',map_range['source_start'],'end val of range:',map_range['source_end'], 'offset: ',map_range['offset'])
        if source_val >= map_range['source_start'] and source_val <= map_range['source_end']:
            dest_val=source_val+map_range['offset']
    dest_type=mapping['dest']
    return dest_val if dest_type == 'location' else traverse_mappings(dest_type, dest_val)

min_location=-1
min_location_seed=0

seed_list=[]
for index, x in enumerate(seed_ranges):
    if index%2==0:
        start_seed=x
    else:
        num_seeds=x
        seed_list.append((start_seed,num_seeds))

for seed_range in seed_list:
    print(seed_range)
    start_seed=int(seed_range[0])
    num_seeds=int(seed_range[1])
    for seed in range(start_seed, start_seed+num_seeds):
        location=traverse_mappings('seed', int(seed))
        # print('seed',seed,'maps to location',location)
        if min_location==-1 or location < min_location:
            min_location=location
            min_location_seed=seed

print(min_location)

f.close()
