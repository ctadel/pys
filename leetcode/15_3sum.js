var threeSum = function(nums) {
    nums.sort((a, b) => a - b); // Sorted Array
    let answer = [];
    
    if (nums.length < 3) {
        return answer;
    }
    
    if (nums[0] > 0) {
        return answer;
    }
    
    let hashMap = new Map();
    
    for (let i = 0; i < nums.length; ++i) {
        hashMap.set(nums[i], i);
    }
    
    for (let i = 0; i < nums.length - 2; ++i) {
        if (nums[i] > 0) {
            break;
        }
        
        for (let j = i + 1; j < nums.length - 1; ++j) {
            let required = -1 * (nums[i] + nums[j]);
            if (hashMap.has(required) && hashMap.get(required) > j) {
                answer.push([nums[i], nums[j], required]);
            }
            j = hashMap.get(nums[j]);
        }
        
        i = hashMap.get(nums[i]);
    }
    
    return answer;
};

nums = [3,0,-2,-1,1,2]
nums = [-1,0,1,2,-1,-4]

data = threeSum(nums)
console.log(data)
