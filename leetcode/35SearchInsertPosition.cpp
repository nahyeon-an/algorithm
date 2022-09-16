#include <iostream>
#include <vector>
#include <string>

using namespace std;

int searchInsert(vector<int> &nums, int target);

int main()
{
  vector<int> nums{1, 3, 5, 7};

  cout << "Input numbers: [ ";

  for (const int &num : nums)
  {
    cout << num << " ";
  }
  cout << "]" << endl;

  for (int i = 0; i < 10; i++)
  {
    cout << endl;
    cout << "Data: " << i << endl;
    cout << "Found Index: " << searchInsert(nums, i) << endl;
  }

  return 0;
}

int searchInsert(vector<int> &nums, int target)
{
  int left = 0;
  int right = nums.size() - 1;

  while (left < right)
  {
    int mid = (left + right) / 2;

    if (nums[mid] == target)
    {
      return mid;
    }
    else if (nums[mid] > target)
    {
      right = mid;
    }
    else if (nums[mid] < target)
    {
      left = mid + 1;
    }
  }
  return left;
}