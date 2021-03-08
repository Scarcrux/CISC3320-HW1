PID Manager Design Documentation

Declare constants for inclusive PID range of 300 to 5000: MIN_PID = 300 and MAX_PID = 5000.

Declare an allocate_map function that creates and initializes a list data structure that represents PIDs in the inclusive range of 300 to 5000. Each element of the list will be set to 0 or 1. 0 indicates PID availability and 1 indicates the PID is in use. This function returns 1 on successful list initialization and returns -1 on list initialization error.

Declare an allocate_pid function that allocates the next available PID. This function searches the PID map for the first element with a value of zero and returns the index. Check and handle the PID map not being initialized and all PIDs being in use. Returns 1 on successful PID allocation and returns -1 on PID allocation error.

Declare a release_pid function that releases a specific PID in the inclusive range of 300 to 5000. This function sets the element for the map data structure to zero and notifies the user if the PID has been released or an error occured (invalid input, PID value outside of range, or the PID map is not initialized). This function has no return value.

Declare a main function that acts as the CLI driver for the API. Use return values from function calls to print user notifications. For allocate_map, notify the user whether the map is initialized or not. For allocate_pid, notify the user of the next available PID or an error. For release_pid, handle non-integer input and call the function. For all menu options, handle invalid input.
